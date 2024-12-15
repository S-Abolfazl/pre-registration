from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from user.models import User
from .models import EducationalChart, CompletedCourses
from .serializers import EducationalChartSerializer
from course.models import AllCourses
from user.permissions import IsStudent
class EducationalChartCreateApi(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
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
    permission_classes = [IsStudent]

    @swagger_auto_schema(
        operation_summary="Educational Chart Get",
        operation_description="Endpoint to get a specific educational chart.",
    )
    def get(self, request):
        try:
            student = request.user
            year = int(student.entry_year)
            if int(student.username[-1]) % 2 == 0:
                type = 'even'
            else:
                type = 'odd'
            chart = EducationalChart.objects.get(year=year, type=type)
            serializer = EducationalChartSerializer(chart)
            data = {}
            course_name = None
            for key, value in serializer.data.items():
                if key == "units" or key == "year" or key == "type" or key == "chart_id":
                    data[key] = value
                    continue            
                try:
                    data[key] = [
                        {
                            "courseName": course_name,
                            "prereq": list(course.prereqs_for.values_list("prereq_course__courseName", flat=True)) if (course := AllCourses.objects.filter(courseName=course_name).first()) else [],
                            "coreq": list(course.coreqs_for.values_list("coreq_course__courseName", flat=True)) if course else [],
                            "unit": course.unit if course else 3,
                            "kind": course.type if course else "elective_course",
                        }
                        for course_name in value
                    ]
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
    permission_classes = [IsStudent, IsAuthenticated]
    @swagger_auto_schema(
        operation_summary="Add Completed Courses",
        operation_description="Endpoint to add a list of completed courses for a student.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'course_ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_STRING),
                    description="List of course IDs to mark as completed",
                ),
            },
            required=['course_ids'],
        ),
    )
    def post(self, request):
        student = request.user
        course_ids = request.data.get('course_ids', [])
        if not course_ids:
            return Response(
                data={
                    "msg": "error",
                    "data": "Course IDs list is required",
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        added_courses = []
        for course_id in course_ids:
            try:
                course = AllCourses.objects.get(course_id=course_id)
                completed_course, created = CompletedCourses.objects.get_or_create(
                    student=student, course=course
                )
                if created:
                    added_courses.append(course.courseName)
            except:
                return Response(
                    {"msg": f"Course with ID {course_id} does not exist."},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(
        {
            "msg": "Courses added successfully.",
            "added_courses": added_courses,
            "status": status.HTTP_200_OK,
        },
        status=status.HTTP_200_OK,
    )
            

class CoursesForPassedCoursesApi(APIView):
    permission_classes = [IsStudent]
    @swagger_auto_schema(
        operation_summary="Get Courses for Passed Courses",
        operation_description="Endpoint to get courses for passed courses for a student.",
    )
    def get(self, request):
        try:
            student = request.user
            year = int(student.entry_year)
            if int(student.username[-1]) % 2 == 0:
                type = 'even'
            else:
                type = 'odd'
                
            chart = EducationalChart.objects.get(year=year, type=type)
            serializer = EducationalChartSerializer(chart)
            data = {}
            for key, value in serializer.data.items():
                if key == "year" or key == "type":
                    data[key] = value
                    continue
                if key == "units" or key == "chart_id":
                    continue            
                try:
                    data[key] = {
                        num: {
                            "id": course.course_id if course else None,
                            "courseName": course_name,
                            "passed": CompletedCourses.objects.filter(student=student, course = course).exists() if course else False,
                        }
                        for num, course_name in enumerate(value, start=1)
                        if (course := AllCourses.objects.filter(
                            courseName=course_name,
                            type__in=['theory_course', 'elective_course', 'practical_course', 'basic_course', 'public_course']
                        ).exclude(courseName__in=["گروه معارف", "دانش خانواده"]).first())
                    }  
                except Exception as e:
                    print(f"Error processing courses in key {key}: {e}")
                
            data["elective_course"] = {
                num:{
                    "id":  course.course_id,
                    "courseName": course.courseName,
                } for num, course in enumerate(AllCourses.objects.filter(
                    type='elective_course'
                ), start=1) 
            }

            return Response(data=data, status=status.HTTP_200_OK)
        except EducationalChart.DoesNotExist:
            return Response(
                data={
                    "msg": "error",
                    "data": f"EducationalChart not found",
                    "status":status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )

