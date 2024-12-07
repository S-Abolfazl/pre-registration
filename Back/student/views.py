from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from user.models import User
from .models import EducationalChart, CompletedCourses
from .serializers import EducationalChartSerializer
from course.models import AllCourses
class EducationalChartCreateApi(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary="Educational Chart Create",
        operation_description="Endpoint to create a new educational chart.",
        request_body=EducationalChartSerializer
    )

    def post(self, request):
        serializer = EducationalChartSerializer(data=request.data)
        if serializer.is_valid():
            chart = serializer.save()
            return Response(
                data={
                    "msg": "ok",
                    "data": f"EducationalChart with id: {chart.chart_id} created successfully",
                    "status":status.HTTP_201_CREATED
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            data={
                "msg": "error",
                "data": serializer.errors,
                "status":status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )
            
class EducationalChartGetApi(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Educational Chart Get",
        operation_description="Endpoint to get a specific educational chart.",
        manual_parameters=[
            openapi.Parameter(
                'year',
                openapi.IN_QUERY,
                description="Year of the educational chart",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'type',
                openapi.IN_QUERY,
                description="Type of the educational chart",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get(self, request):
        try:
            year = int(request.query_params.get('year'))
            type = request.query_params.get('type')
            chart = EducationalChart.objects.get(year=year, type=type)
            serializer = EducationalChartSerializer(chart)
            data = {}
            course_name = None
            for key, value in serializer.data.items():
                if key == "units" or key == "year" or key == "type" or key == "chart_id":
                    data[key] = value
                    continue            
                try:
                    data[key] = {
                        course_name: (
                            {
                                "prereq": list(course.prereqs_for.values_list("prereq_course__courseName", flat=True)),
                                "coreq": list(course.coreqs_for.values_list("coreq_course__courseName", flat=True)),
                                "unit": course.unit,
                                "kind": course.type
                            } if (course := AllCourses.objects.filter(courseName=course_name).first()) else {
                                "prereq": [],
                                "coreq": [],
                                "unit": 3,
                                "kind": "elective_course"
                            }
                        )
                        for course_name in value
                    }
                except Exception as e:
                    print(f"Error processing courses in key {key}: {e}")
                    
            return Response(data=data, status=status.HTTP_200_OK)
        except EducationalChart.DoesNotExist:
            return Response(
                data={
                    "msg": "error",
                    "data": f"EducationalChart not found {course_name}",
                    "status":status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )
        

class AddCompletedCourseApi(APIView):
    @swagger_auto_schema(
        operation_summary="Add Completed Courses",
        operation_description="Endpoint to add a list of completed courses for a student.",
        manual_parameters=[
            openapi.Parameter(
                'student_id',
                openapi.IN_QUERY,
                description="ID of the student",
                type=openapi.TYPE_INTEGER,
                required=True,
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'course_ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description="List of course IDs to mark as completed",
                ),
            },
            required=['course_ids'],
        ),
    )
    def post(self, request):
        student_id = request.query_params.get('student_id')
        course_ids = request.data.get('course_ids', [])
        if not student_id:
            return Response(
                data={
                    "msg": "error",
                    "data": "Student ID is required",
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not course_ids:
            return Response(
                data={
                    "msg": "error",
                    "data": "Course IDs list is required",
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        student = request.user
        added_courses = []
        for course_id in course_ids:
            try:
                course = AllCourses.objects.get(id=course_id)
                # Create or get the CompletedCourse record
                completed_course, created = CompletedCourses.objects.get_or_create(
                    student=student, course=course
                )
                if created:
                    added_courses.append(course.courseName)
            except AllCourses.DoesNotExist:
                return Response(
                    {"msg": f"Course with ID {course_id} does not exist."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return Response(
            {
                "msg": "Courses added successfully.",
                "added_courses": added_courses,
            },
            status=status.HTTP_200_OK,
        )
    