from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import RegistrationForm
from course.models import Course, AllCourses
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
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                'msg': 'error',
                'data': serializer.errors
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
    
    
    
    def get(self, request):
        try:
            student_id = request.user.id
            courses = Course.objects.all()
            completed_courses = CompletedCourses.objects.filter(student_id=student_id)
            for com_course in completed_courses:
                courses = courses.exclude(course_id=com_course.course_id)
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
                    'data': 'Error in getting courses: ' + str(e),
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )