from rest_framework import serializers
from .PersianModelserializer import PersianModelserializer

from .models import Course, AllCourses

class CourseSerializer(PersianModelserializer): 
    class Meta:
        model = Course
        fields = '__all__'

class AllCoursesSerializer(PersianModelserializer):
    class Meta:
        model = AllCourses
        fields = '__all__'       