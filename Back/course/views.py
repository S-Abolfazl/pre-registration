from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import User
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
