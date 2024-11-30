from rest_framework import serializers

from .models import Course, AllCourses

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AllCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCourses
        fields = '__all__'       