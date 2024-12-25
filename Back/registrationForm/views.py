from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import RegistrationForm, SelectedCourse
from course.models import Course, AllCourses, Prereq, Coreq
from student.models import CompletedCourses
from .serializers import RegistrationFormSerializer, RegisterationFormDetailSerializer
from user.permissions import IsStudentOrAdmin, IsStudent


class RegistrationFormListView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    @swagger_auto_schema(
        operation_summary="Get Registration Forms",
        operation_description="Endpoint to get all registration forms or a single registration form.",
    )
    
    def get(self, request, form_id=None):
        if form_id:
            try:
                form = RegistrationForm.objects.get(form_id=form_id)
                serializer = RegisterationFormDetailSerializer(form)
            except:
                return Response(
                    data={
                        'msg': 'error',
                        'data': f'Registration form {form_id} not found',
                        "status": status.HTTP_404_NOT_FOUND
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            forms = RegistrationForm.objects.all()
            serializer = RegisterationFormDetailSerializer(forms, many=True)

        return Response(
            data={
                'msg': 'ok',
                'data': serializer.data,
                "status": status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )


class RegistrationFormCreateView(APIView):
    permission_classes = (IsAuthenticated, IsStudent)
    
    @swagger_auto_schema(
        operation_summary="Create Registration Form",
        operation_description="Endpoint to create a new registration form.",
    )

    def post(self, request):
        user_id = request.user.id

        data = request.data.copy()
        data['student_id'] = user_id

        serializer = RegistrationFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    'msg': 'ok',
                    'data': serializer.data,
                    "status": status.HTTP_201_CREATED
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                'msg': 'error',
                'data': serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class RegistrationFormUpdateView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    @swagger_auto_schema(
        operation_summary="Update Registration Form",
        operation_description="Endpoint to update a registration form.",
        request_body=RegistrationFormSerializer,
    )
    def put(self, request, form_id):
        form = get_object_or_404(RegistrationForm, form_id=form_id)
        serializer = RegistrationFormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    'msg': 'ok',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'msg': 'error',
                'data': serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class RegistrationFormDeleteView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    
    @swagger_auto_schema(
        operation_summary="Delete Registration Form",
        operation_description="Endpoint to delete a registration form.",
    )

    def delete(self, request, form_id):
        form = get_object_or_404(RegistrationForm, form_id=form_id)
        form.delete()
        return Response(
            data={
                'msg': 'ok',
                'data': f'Registration form {form_id} deleted successfully',
                "status": status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )


class RegistrationFormDataApi(APIView):
    permission_classes = (IsAuthenticated, IsStudent)
    
    @swagger_auto_schema(
        operation_summary="Get Registration Form Data",
        operation_description="Endpoint to get data for registration form.",
    )
    
    def get(self, request):
        try:
            student_id = request.user.id
            courses = Course.objects.all()
            completed_courses = CompletedCourses.objects.filter(student_id=student_id)
            selected_courses = SelectedCourse.objects.filter(form__student_id=student_id)
            selected_courses = selected_courses.values_list('course_id', flat=True)
            for com_course in completed_courses:
                courses = courses.exclude(course=com_course.course_id)
            courses = courses.values()
            for c in courses:
                course = AllCourses.objects.get(course_id=c['course_id'])
                c.pop('course_id')
                c['course'] = {
                    'course_id': course.course_id,
                    'courseName': course.courseName,
                    'unit': course.unit,
                    'type': course.type
                }
                c['class_start_time'] = str(c['class_start_time'])[:-3]
                c['class_end_time'] = str(c['class_end_time'])[:-3]
                c['exam_start_time'] = str(c['exam_start_time'])[:-3]
                c['exam_end_time'] = str(c['exam_end_time'])[:-3]
                c['selected'] = True if c['c_id'] in selected_courses else False
            return Response(
                data={
                    'msg': 'ok',
                    'data': courses,
                    "status": status.HTTP_200_OK
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                data={
                    'msg': 'error',
                    'data': 'مشکلی در دریافت اطلاعات دروس پیش ثبت نام به وجود آمده است',
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
class RegistrationFormConfirmApi(APIView):
    permission_classes = (IsAuthenticated, IsStudent)
    
    @swagger_auto_schema(
        operation_summary="Confirm Registration Form",
        operation_description="Endpoint to confirm registration form and add selected courses.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'course_ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_STRING),
                    description="List of course IDs selected for registration",
                ),
            },
            required=['course_ids'],
        ),
    )
    
    def post(self, request):
        try:
            student_id = request.user.id
            course_ids = request.data.get('course_ids', [])
            if not course_ids:
                selected_courses = SelectedCourse.objects.filter(form__student_id=student_id).values_list('course', flat=True)
                for c_id in selected_courses:
                    course = Course.objects.get(c_id=c_id)
                    course.registered -= 1
                    course.save()
                SelectedCourse.objects.filter(form__student_id=student_id).delete()
                return Response(
                    data={
                        'msg': 'ok',
                        'data': 'تمامی دروس انتخاب شده حذف شدند',
                        "status": status.HTTP_200_OK
                    }, 
                    status=status.HTTP_200_OK
                )
            form = RegistrationForm.objects.get(student_id=student_id)
            
            before_selected_course = SelectedCourse.objects.filter(form=form).values_list('course', flat=True)
            
            for course_id in before_selected_course:
                if str(course_id) not in course_ids:
                    SelectedCourse.objects.get(form=form, course_id=course_id).delete()
                    course = Course.objects.get(c_id=course_id)
                    course.registered -= 1
                    course.save()
            
            for course_id in course_ids:
                course = Course.objects.get(c_id=course_id)
                base_course = course.course
                prerequisites = Prereq.objects.filter(course=base_course)
                prerequisites = prerequisites.values_list('prereq_course', flat=True)
                completed_courses = CompletedCourses.objects.filter(student=student_id).values_list('course', flat=True)
                if not all(prereq in completed_courses for prereq in prerequisites):
                    return Response(
                        data={
                            'msg': 'error',
                            'data': f"شما تمام پیشنیازهای درس {course.course.courseName} نگذرانده‌اید",
                            "status": status.HTTP_400_BAD_REQUEST
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
               
                if not SelectedCourse.objects.filter(form=form, course=course).exists(): 
                    SelectedCourse.objects.create(form=form, course=course)
                    course.registered += 1
                    course.save()
                
                
            return Response(
                data={
                    'msg': 'ok',
                    'data': 'دروس انتخاب شده با موفقیت ثبت شدند',
                    "status": status.HTTP_201_CREATED
                },
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                data={
                    'msg': 'error',
                    'data': 'مشکلی در ثبت دروس انتخاب شده برای پیش ثبت نام به وجود آمده است',
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )