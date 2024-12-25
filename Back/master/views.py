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
    
   # class MasterListApi(APIView):
    #    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
     #   @swagger_auto_schema(
      #      operation_summary="Masters List",
       #     operation_description="Endpoint to list all masters"
        #)
        #def get(self, request, pk = None):
         #   try:
          #      if pk:
           #         master = master.objects.get(c_id = pk)
            #        serializer = MasterSerializer(master)
             #   else:
              #      master = master.objects.all()
               #     serializer = MasterSerializer(master,many = True)
             #   return Response(data = serializer.data, status = status.HTTP_200_ok)
            #except Master
class MasteeDeleteApi(APIView):
    permission_classes = [AllowAny, IsAdminUser]
    @swagger_auto_schema(
        operation_summary = "Master Delete",
        operation_description = "Endpoint to delete a master by id.",
        request_body = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['id'],
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Master ID')
            }
        )
    )
    def delete(self, request, pk):
        try:
            Master = Master.objects.get(id=pk)
            Master.delete()
            return Response(data={
                "msg":"ok",
                "data":f'master by id:{pk} deleted',
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except Master.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"master not found",
                "status": status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={
                "msg":"error",
                "data":str(e),
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
        


class MasterUpdateApi(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(
        operation_summary="master Patch",
        operation_description="Endpoint to partially update a master by id, including uploading an avatar.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'education': openapi.Schema(type=openapi.TYPE_STRING, description='education'),
                'department': openapi.Schema(type=openapi.TYPE_STRING, description='department'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
                'rate': openapi.Schema(type=openapi.TYPE_STRING, description='rate'),
                'Master_type': openapi.Schema(type=openapi.TYPE_STRING, description='Master_type'),
                'specialization': openapi.Schema(type=openapi.TYPE_STRING, description='specialization'),
                'mobile_number': openapi.Schema(type=openapi.TYPE_STRING, description='Mobile number'),
                'avatar': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="binary",
                    description="Upload an avatar image"
                )
            },
        )
    )
    def patch(self, request):
        try:
            master = request.master
            serializer = MasterSerializer(master, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(data = {
                    "msg": "ok",
                    "data": f'master by id:{master.id} updated',
                    "status": status.HTTP_200_OK
                }, status=status.HTTP_200_OK)
            return Response(
                data={
                    "msg": "error",
                    "data": serializer.errors,
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Master.DoesNotExist:
            return Response(data={
                "msg": "error",
                "data": "master not found",
                "status": status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={
                "msg": "error",
                "data": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
            