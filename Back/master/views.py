from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Master
from django.views.decorators.csrf import csrf_exempt

from .models import Course, AllCourses
from .serializers import MasterSerializer, AllCoursesSerializer, CourseDetailSerializer, AllCoursesDetailSerializer
from user.permissions import IsAcademicAssistantOrAdmin, IsStudentOrIsAcademicAssistantOrAdmin
from django.views.decorators.csrf import csrf_exempt


class MasterCreateView(APIView):
    permission_classes = [IsAuthenticated]  # فقط کاربران احراز هویت شده اجازه دسترسی دارند

    @swagger_auto_schema(
        operation_summary="Master Create",
        operation_description="Endpoint to create a new master (professor).",
        request_body=MasterSerializer
    )
    def post(self, request):
        request_data = request.data.copy()

        serializer = MasterSerializer(data=request_data)
        if serializer.is_valid():
            try:
                master = serializer.save()
                return Response(
                    data={
                        "msg": "ok",
                        "data": f'Master {master.first_name} {master.last_name} created successfully.',
                        "status": status.HTTP_201_CREATED
                    },
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    data={
                        "msg": "error",
                        "data": f"An error occurred while saving the master: {str(e)}",
                        "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(
            data={
                "msg": "error",
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )