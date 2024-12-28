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
    permission_classes = [IsStudent, IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Educational Chart Get",
        operation_description="Endpoint to get a specific educational chart.",
    )
    def get(self, request):
        student = request.user
        year = int(student.entry_year)
        if int(student.username[-1]) % 2 == 0:
            type = 'even'
        else:
            type = 'odd'
        try:
            chart = EducationalChart.objects.get(year=year, type=type)
        except:
            return Response(
                data={
                    "msg": "error",
                    "data": f"چارت درسی ای مربوط به ورودی شما یافت نشد",
                    "status":status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = EducationalChartSerializer(chart)
        data = {}
        data['terms'] = {}
        term = 1
        course_name = None
        for key, value in serializer.data.items():
            if key == "units" or key == "year" or key == "type" or key == "chart_id":
                data[key] = value
                continue            
            try:
                data['terms'][term] = [
                    {
                        "courseName": course_name,
                        "prereq": list(course.prereqs_for.values_list("prereq_course__courseName", flat=True)) if (course := AllCourses.objects.filter(courseName=course_name).first()) else [],
                        "coreq": list(course.coreqs_for.values_list("coreq_course__courseName", flat=True)) if course else [],
                        "unit": course.unit,
                        "kind": course.type,
                        "course_id": course.course_id,
                    }
                    for course_name in value
                ]
                
                term += 1
            except Exception as e:
                return Response(
                    data={
                        "msg": "error",
                        "data": f"خطاای در پردازش درس ها رخ داده است",
                        "status":status.HTTP_500_INTERNAL_SERVER_ERROR
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
                
        return Response(data={
                "msg": "ok",
                "data": data,
                "status":status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

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
            CompletedCourses.objects.filter(student=student).delete()
            return Response(
                data={
                    "msg": "ok",
                    "data": "تمامی دروس گذرانده شده حذف شدند",
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        completed_before = CompletedCourses.objects.filter(student=student).values_list("course", flat=True)
        for course_id in completed_before:
            if str(course_id) not in course_ids:
                CompletedCourses.objects.filter(student=student, course=course_id).delete()
            
        completed_courses = []
        for course_id in course_ids:
            try:
                course = AllCourses.objects.get(course_id=course_id)
                CompletedCourses.objects.get_or_create(
                    student=student, course=course
                )
                completed_courses.append(course.courseName)
            except:
                return Response(
                    {"msg": f"Course with ID {course_id} does not exist"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(
       data={
            "msg": "درس های انتخاب شده با موفقیت به لیست دروس گذارتده شده اضافه شدند",
            "completed_courses": completed_courses,
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
            data["terms"] = {}
            for key, value in serializer.data.items():
                if key == "year" or key == "type":
                    data[key] = value
                    continue
                if key == "units" or key == "chart_id":
                    continue            
                try:
                    data["terms"][key[-1]] = {}
                    num = 1
                    for course_name in value:
                        course = AllCourses.objects.filter(
                            courseName=course_name,
                            type__in=['theory_course', 'elective_course', 'practical_course', 'basic_course', 'public_course']
                        ).exclude(courseName__in=["گروه معارف", "دانش خانواده"]).first()
                        
                        if course:
                            data["terms"][key[-1]][num] = {
                                "id": course.course_id,
                                "courseName": course_name,
                                "passed": CompletedCourses.objects.filter(student=student, course=course).exists(),
                            }
                            num += 1  
                except Exception as e:
                    return Response(
                        data={
                            "msg": "error",
                            "data": f"خطاای در پردازش درس ها رخ داده است",
                            "status":status.HTTP_500_INTERNAL_SERVER_ERROR
                        },
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
                
            data["elective_course"] = {
                num:{
                    "id":  course.course_id,
                    "courseName": course.courseName,
                } for num, course in enumerate(AllCourses.objects.filter(
                    type='elective_course'
                ), start=1) 
            }

            return Response(data={
                "msg": "ok",
                "data": data,
                "status":status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except EducationalChart.DoesNotExist:
            return Response(
                data={
                    "msg": "error",
                    "data": f"چارت درسی ای مربوط به ورودی شما یافت نشد",
                    "status":status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )
            
class CompletedCoursesApi(APIView):
    permission_classes = [IsStudent, IsAuthenticated]
    @swagger_auto_schema(
        operation_summary="Get Completed Courses",
        operation_description="Endpoint to get list of completed courses for a student.",
    )
    def get(self, request):
        student = request.user
        completed_courses = CompletedCourses.objects.filter(student=student)
        data = {
            "completed_courses": [
                {
                    "course_id": course.course.course_id,
                    "course_name": course.course.courseName,
                    "unit": course.course.unit,
                    "type": course.course.type,
                }
                for course in completed_courses
            ]
        }
        return Response(data={
            "msg": "ok",
            "data": data,
            "status": status.HTTP_200_OK    
        }, status=status.HTTP_200_OK)

