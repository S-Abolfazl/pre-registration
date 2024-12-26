from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Count
from  user.permissions import IsAcademicAssistantOrAdmin, IsAcademicAssistant
from course.models import Course, AllCourses
from user.models import User
from registrationForm.models import RegistrationForm 

class StatisticsBarChartApi(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Statistics Bar Chart API", 
        operation_description="This API returns the number of students registered in each course and datas to show in a bar chart",
    )
    
    def get(self, request):
        courses = Course.objects.all()
        
        data = []
        
        try:
            for course in courses:
                class_start_end = ""
                if course.class_start_time and course.class_end_time:
                    start = course.class_start_time.strftime("%H:%M")
                    end = course.class_end_time.strftime("%H:%M") 
                    class_start_end = f"{start} - {end}"
                data.append({
                    'courseName': course.course.courseName,
                    'teacherName': course.teacherName,
                    'class_time1': course.class_time1 if course.class_time1 else "",
                    'class_time2': course.class_time2 if course.class_time1 else "",
                    'class_start_end': class_start_end,
                    'capacity': course.capacity,
                    'registered': course.registered,
                })
        except:
            return Response(data={
                "msg":"error",
                "data":"مشکلی در دریافت اطلاعات به وجود آمده است",
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        
        return Response(data={
            "msg":"ok",
            "data":data,
            "status":status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
        
             
class StatisticsParticipationPercent(APIView):
    permission_classes = [IsAcademicAssistantOrAdmin, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Statistics Participation Percent API",
        operation_description="This API returns the percentage of students who have participated in pre registration",
    )
    
    def get(self, request):
        try:
            student_users_by_entry_year = (
                User.objects.filter(type="student")
                .values("entry_year")
                .annotate(count=Count("id"))
                .order_by("entry_year")
            )
            
            participated_users_by_endtry_year = (
                RegistrationForm.objects.all()
                .values("student_id__entry_year")
                .annotate(count=Count("form_id"))
                .order_by("student_id__entry_year")
            )
            
            print(student_users_by_entry_year)
            print(participated_users_by_endtry_year)
            
            return Response(data={}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={
                "msg":"error",
                "data":"مشکلی در دریافت اطلاعات به وجود آمده است" + " " + str(e),
                "status":status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)    
        