from rest_framework import serializers
from .PersianModelserializer import PersianModelserializer

from .models import Course, AllCourses, CourseRule

class CourseSerializer(PersianModelserializer): 
    class Meta:
        model = Course
        fields = ['course', 'teacherName', 'isExperimental', 'class_time1', 'class_time2', 'class_start_time', 'class_end_time', 'exam_date', 'exam_start_time', 'exam_end_time', 'capacity']

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AllCoursesSerializer(PersianModelserializer):
    class Meta:
        model = AllCourses
        fields = ['courseName', 'unit', 'type']
        
        
class AllCoursesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCourses
        fields = '__all__'
        
class CourseRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRule
        fields = '__all__'       