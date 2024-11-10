from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Course
from .serializers import CourseSerializer

from django.views.decorators.csrf import csrf_exempt

class CourseCreateApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            return Response(data={
                "msg":"ok",
                "data":f'course by id:{course.id} created'
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class CourseListApi(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk=None):
        try:
            if pk:
                course = Course.objects.get(id=pk)
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