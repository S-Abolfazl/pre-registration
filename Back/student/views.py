from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from .models import EducationalChart
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
            

class CoursesForPassedCoursesApi(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary="Courses For Passed Courses",
        operation_description="Endpoint to get courses for passed courses.",
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
            for key, value in serializer.data.items():
                if key == "year" or key == "type":
                    data[key] = value
                    continue
                if key == "units" or key == "chart_id":
                    continue            
                try:
                    data[key] = {
                        str(num): {
                            "id": course.course_id if course else None,
                            "courseName": course_name,
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
                str(num):{
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