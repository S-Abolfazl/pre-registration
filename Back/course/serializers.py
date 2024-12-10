from rest_framework import serializers

from .models import Course, AllCourses

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course', 'teacherName', 'isExperimental', 'class_time1', 'class_time2', 'class_start_time', 'class_end_time', 'exam_date', 'exam_start_time', 'exam_end_time', 'capacity']

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AllCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCourses
        fields = ['courseName', 'unit', 'type']
        
        
class AllCoursesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCourses
        fields = '__all__'       