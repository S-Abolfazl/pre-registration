from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Course, AllCourses
from .serializers import CourseSerializer, AllCoursesSerializer
from user.permissions import IsAcademicAssistantOrAdmin
from django.views.decorators.csrf import csrf_exempt

class CourseCreateApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin]
    @swagger_auto_schema(
        operation_summary="Course Create",
        operation_description="Endpoint to create a new course in term.",
        request_body=CourseSerializer
    )
    def post(self, request):
        
        course_instance = get_object_or_404(AllCourses, course_id=request.data['course'])
        
        request_data = request.data.copy()
        request_data['course'] = course_instance.course_id
        
        serializer = CourseSerializer(data=request_data)
        if serializer.is_valid():
            course = serializer.save()
            return Response(data={
                "msg":"ok",
                "data":f'course by id:{course.c_id} created'
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class CourseListApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin]
    
    @swagger_auto_schema(
        operation_summary="Course List",
        operation_description="Endpoint to list all courses in term."
    )
    
    def get(self, request, pk=None):
        try:
            if pk:
                course = Course.objects.get(c_id=pk)
                serializer = CourseSerializer(course)
            else:
                courses = Course.objects.all()
                serializer = CourseSerializer(courses, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
class CourseUpdateApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin]
    
    @swagger_auto_schema(
        operation_summary="Course Update",
        operation_description="Endpoint to update a course in term.",
        request_body=CourseSerializer
    )
    def put(self, request, pk):
        try:
            course = Course.objects.get(c_id=pk)
            c = AllCourses.objects.get(course_id=request.data['course'])
            request_data = request.data.copy()
            request_data['course'] = c.course_id
            serializer = CourseSerializer(course, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={
                    "msg":"ok",
                    "data":f'course by id:{course.c_id} updated',
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
        except Course.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        operation_summary="Course Update",
        operation_description="Endpoint to update a course in term partialy.",
        request_body=CourseSerializer
    )        
    def patch(self, request, pk):
        try:
            course = Course.objects.get(c_id=pk)
            c = AllCourses.objects.get(course_id=request.data['course'])
            request_data = request.data.copy()
            request_data['course'] = c.course_id
            serializer = CourseSerializer(course, data=request_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data={
                    "msg":"ok",
                    "data":f'course by id:{course.c_id} updated',
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
        except Course.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found"
            }, status=status.HTTP_404_NOT_FOUND)
        
class CourseDeleteApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin]
    
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
                "data":f'course by id:{pk} deleted',
                "status":status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
            
class AllCourseCreateApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin]
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
    permission_classes = [IsAcademicAssistantOrAdmin]
    
    @swagger_auto_schema(
        operation_summary="Course List",
        operation_description="Endpoint to list all courses."
    )
    
    def get(self, request, pk=None):
        try:
            if pk:
                course = AllCourses.objects.get(course_id=pk)
                serializer = AllCoursesSerializer(course)
            else:
                courses = AllCourses.objects.all()
                serializer = AllCoursesSerializer(courses, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except AllCourses.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"course not found",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
            
class AllCourseUpdateApi(APIView):
    permission_classes = [AllowAny]
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
    
            
class AllCourseDeleteApi(APIView):
    permission_classes = [AllowAny]
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