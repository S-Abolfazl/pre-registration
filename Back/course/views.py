from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Course, AllCourses, CourseRule
from .serializers import CourseSerializer, AllCoursesSerializer, CourseDetailSerializer, AllCoursesDetailSerializer, CourseRuleSerializer
from user.permissions import IsAcademicAssistantOrAdmin, IsStudentOrIsAcademicAssistantOrAdmin
from django.views.decorators.csrf import csrf_exempt

class CourseCreateApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    @swagger_auto_schema(
        operation_summary="Course Create",
        operation_description="Endpoint to create a new course in term.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'courseName': openapi.Schema(type=openapi.TYPE_STRING, description='course name'),
                'teacherName': openapi.Schema(type=openapi.TYPE_STRING, description='teacher name'),
                'isExperimental': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='is experimental'),
                'class_time1': openapi.Schema(type=openapi.TYPE_STRING, description='class time1'),
                'class_time2': openapi.Schema(type=openapi.TYPE_STRING, description='class time2'),
                'class_start_time': openapi.Schema(type=openapi.TYPE_STRING, description='class start time'),
                'class_end_time': openapi.Schema(type=openapi.TYPE_STRING, description='class end time'),
                'exam_date': openapi.Schema(type=openapi.TYPE_STRING, description='exam date'),
                'exam_start_time': openapi.Schema(type=openapi.TYPE_STRING, description='exam start time'),
                'exam_end_time': openapi.Schema(type=openapi.TYPE_STRING, description='exam end time'),
                'capacity': openapi.Schema(type=openapi.TYPE_INTEGER, description='capacity'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),
                'entry_years': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING), description='entry years'),
            }
        )
    )
    def post(self, request):
        
        try:
            course_instance = AllCourses.objects.get(courseName=request.data['courseName'])
        except Exception as e:
            return Response(data={
                "msg":"error",
                "data":"درس مورد نظر یافت نشد",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
            
        request_data = request.data.copy()
        request_data.pop('courseName', None)
        request_data['course'] = course_instance.course_id
        
        serializer = CourseSerializer(data=request_data)
        if serializer.is_valid():
            course = serializer.save()
            entry_years = request.data['entry_years']
            if entry_years:
                entry_years = [year[-3:] if year[:2] == "14" else year[-2:] for year in entry_years]
                course_rule = CourseRuleSerializer(data={
                    'course': course.c_id,
                    'type': 'entry_rule',
                    'values': entry_years,
                })
                if course_rule.is_valid():
                    course_rule.save()
                else:
                    return Response(data={
                        "msg":"error",
                        "data":course_rule.errors,
                        "status":status.HTTP_400_BAD_REQUEST
                    }, status=status.HTTP_400_BAD_REQUEST)
            return Response(data={
                "msg":"ok",
                "data":f'درس با شناسه:{course.c_id} ایجاد شد',
                "status":status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors,
                "status":status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class CourseListApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Course List",
        operation_description="Endpoint to list all courses in term."
    )
    
    def get(self, request, pk=None):
        try:
            if pk:
                course = Course.objects.get(c_id=pk)
                serializer = CourseDetailSerializer(course)
                data = serializer.data
                course_rules = CourseRule.objects.filter(course=course.c_id)
                for rule in course_rules:
                    if rule.type == 'entry_rule':
                        data['entry_years'] = rule.values
            else:
                courses = Course.objects.all()
                serializer = CourseDetailSerializer(courses, many=True)
                course_rules = CourseRule.objects.all()
                data = serializer.data
                for course in data:
                    rules = course_rules.filter(course=course['c_id'])
                    for rule in rules:
                        if rule.type == 'entry_rule':
                            course['entry_years'] = rule.values 
                    
            return Response(data=data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"درس مورد نظر یافت نشد",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response(data={
                "msg":"error",
                "data":"شناسه درس معتبر نیست",
                "status":status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
        
class CourseUpdateApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Course Update",
        operation_description="Endpoint to update a course in term.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'courseName': openapi.Schema(type=openapi.TYPE_STRING, description='course name'),
                'teacherName': openapi.Schema(type=openapi.TYPE_STRING, description='teacher name'),
                'isExperimental': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='is experimental'),
                'class_time1': openapi.Schema(type=openapi.TYPE_STRING, description='class time1'),
                'class_time2': openapi.Schema(type=openapi.TYPE_STRING, description='class time2'),
                'class_start_time': openapi.Schema(type=openapi.TYPE_STRING, description='class start time'),
                'class_end_time': openapi.Schema(type=openapi.TYPE_STRING, description='class end time'),
                'exam_date': openapi.Schema(type=openapi.TYPE_STRING, description='exam date'),
                'exam_start_time': openapi.Schema(type=openapi.TYPE_STRING, description='exam start time'),
                'exam_end_time': openapi.Schema(type=openapi.TYPE_STRING, description='exam end time'),
                'capacity': openapi.Schema(type=openapi.TYPE_INTEGER, description='capacity'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),
                'entry_years': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING), description='entry years'),
            }
        )
    )
    def patch(self, request, pk):
        try:
            course = Course.objects.get(c_id=pk)
            c = AllCourses.objects.get(courseName=request.data['courseName'])
            request_data = request.data.copy()
            request_data['course'] = c.course_id
            request_data.pop('courseName', None)
            if 'entry_years' in request_data:
                request_data.pop('entry_years', None)
            serializer = CourseSerializer(course, data=request_data)
            if serializer.is_valid():
                serializer.save()
                entry_years = request.data['entry_years']
                if entry_years:
                    entry_years = [year[-3:] if year[:2] == "14" else year[-2:] for year in entry_years]
                    course_rule = CourseRule.objects.filter(course=course.c_id, type='entry_rule')
                    if course_rule.exists():
                        course_rule.update(values=entry_years)
                    else:
                        course_rule = CourseRuleSerializer(data={
                            'course': course.c_id,
                            'type': 'entry_rule',
                            'values': entry_years,
                        })
                        if course_rule.is_valid():
                            course_rule.save()
                        else:
                            return Response(data={
                                "msg":"error",
                                "data":course_rule.errors,
                                "status":status.HTTP_400_BAD_REQUEST
                            }, status=status.HTTP_400_BAD_REQUEST)
                else:
                    CourseRule.objects.filter(course=course.c_id, type='entry_rule').delete()
                        
                return Response(data={
                    "msg":"ok",
                    "data":f'درس با شناسه:{course.c_id} به روز شد',
                    "status":status.HTTP_200_OK
                }, status=status.HTTP_200_OK)
            return Response(
                data={
                    "msg":"error",
                    "data": serializer.errors,
                    "satatus":status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(data={
                "msg":"error",
                "data":"درس مورد نظر یافت نشد ",
            }, status=status.HTTP_404_NOT_FOUND)
        
class CourseDeleteApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Course Delete",
        operation_description="Endpoint to delete a course in term."
    )
        
    def delete(self, request, pk):
        try:
            course = Course.objects.get(c_id=pk)
            course.delete()
            return Response(data={
                "msg":"ok",
                "data":f'درس با شناسه:{pk} حذف شد',
                "status":status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"درس مورد نظر یافت نشد",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response(data={
                "msg":"error",
                "data":"شناسه درس معتبر نیست",
                "status":status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)

class AllCourseCreateApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    @swagger_auto_schema(
        operation_summary="Course Create",
        operation_description="Endpoint to create a new course.",
        request_body=AllCoursesSerializer
    )
    def post(self, request):
        serializer = AllCoursesSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            return Response(data={
                "msg":"ok",
                "data":f'course by id:{course.course_id} created',
                "status":status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors,
                "status":status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class AllCourseListApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Course List",
        operation_description="Endpoint to list all courses."
    )
    
    def get(self, request, pk=None):
        try:
            if pk:
                course = AllCourses.objects.get(course_id=pk)
                serializer = AllCoursesDetailSerializer(course)
            else:
                courses = AllCourses.objects.all()
                serializer = AllCoursesDetailSerializer(courses, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except AllCourses.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response(data={
                "msg":"error",
                "data":"id validation error",
                "status":status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
            
class AllCourseUpdateApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Course Update",
        operation_description="Endpoint to update a course.",
        request_body=AllCoursesSerializer
    )
    def put(self, request, pk):
        try:
            course = AllCourses.objects.get(course_id=pk)
            serializer = AllCoursesSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={
                    "msg":"ok",
                    "data":f'course by id:{course.course_id} updated',
                    "status":status.HTTP_200_OK
                }, status=status.HTTP_200_OK)
            return Response(
                data={
                    "msg":"error",
                    "data": serializer.errors,
                    "status":status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except AllCourses.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response(data={
                "msg":"error",
                "data":"id validation error",
                "status":status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
            
    @swagger_auto_schema(
        operation_summary="Course Update",
        operation_description="Endpoint to update a course partialy.",
        request_body=AllCoursesSerializer
    )
    def patch(self, request, pk):
        try:
            course = AllCourses.objects.get(course_id=pk)
            serializer = AllCoursesSerializer(course, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data={
                    "msg":"ok",
                    "data":f'course by id:{course.course_id} updated',
                    "status":status.HTTP_200_OK
                }, status=status.HTTP_200_OK)
            return Response(
                data={
                    "msg":"error",
                    "data": serializer.errors,
                    "status":status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except AllCourses.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
    
            
class AllCourseDeleteApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Course Delete",
        operation_description="Endpoint to delete a course."
    )
    def delete(self, request, pk):
        try:
            course = AllCourses.objects.get(course_id=pk)
            course.delete()
            return Response(data={
                "msg":"ok",
                "data":f'course by id:{pk} deleted',
                "status":status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except AllCourses.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response(data={
                "msg":"error",
                "data":"id validation error",
                "status":status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
            
            
class CourseinTermApi(APIView):
    permission_classes = [IsAuthenticated, IsStudentOrIsAcademicAssistantOrAdmin]

    @swagger_auto_schema(
        operation_summary="Courses Offered",
        operation_description="API to get the courses offered in a specific term.",
    )
    def get(self, request):

        courses = Course.objects.all()

        data = []
        for course in courses:
            class_schedule = (
                f"{course.class_time1}"
            ) if course.class_time1 else ''
            
            if course.class_time2 and course.class_time2 != course.class_time1:
                class_schedule += (
                    f"-{course.class_time2 or '-'}"
                )
            else:
                class_schedule += (
                    f" ها"
                )
            
            if course.class_start_time and course.class_end_time:
                class_schedule += (
                    f" {str(course.class_start_time)[:-3]} - {str(course.class_end_time)[:-3]}"
                )

            exam_schedule = (
                f"تاریخ: {course.exam_date} "
                f"ساعت: {str(course.exam_start_time)[:-3]} - {str(course.exam_end_time)[:-3]}"
            ) if course.exam_date else ''

            combined_schedule = ""

            if class_schedule:
                combined_schedule += f"کلاس: {class_schedule}"
            
            if exam_schedule:
                combined_schedule += f" | امتحان: {exam_schedule} "
                
            course_data = {
                "c_id": course.c_id,
                "courseName": course.course.courseName,
                "unit": course.course.unit,
                "type": course.course.type,
                "capacity": course.capacity,
                "teacher": course.teacherName,
                "schedule": combined_schedule,
                "description": course.description or "ندارد",
            }
            data.append(course_data)

        return Response(data={
                "msg": "ok",
                "data": data,
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)