from django.contrib import admin
from .models import Course, AllCourses, Prereq, Coreq, CourseRule
from django import forms
from django.urls import reverse
from django.utils.html import format_html


@admin.register(AllCourses)
class AllCoursesAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'courseName', 'unit', 'type')
    search_fields = ('courseName',)
    list_filter = ('type',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'course', 'teacherName', 'display_class_time1', 'display_class_time2', 
                    'display_class_start_time', 'display_class_end_time', 'isExperimental', 'capacity', 'registered')
    
    search_fields = ('course__courseName', 'teacherName')
    list_filter = ('isExperimental', 'class_time1', 'class_time2')
    
    def display_class_time1(self, obj):
        return obj.class_time1
    display_class_time1.short_description = 'Class Time 1'
    
    def display_class_time2(self, obj):
        return obj.class_time2
    display_class_time2.short_description = 'Class Time 2'
    
    def display_class_start_time(self, obj):
        return obj.class_start_time
    display_class_start_time.short_description = 'Class Start Time'
    
    def display_class_end_time(self, obj):
        return obj.class_end_time
    display_class_end_time.short_description = 'Class End Time'


@admin.register(Prereq)
class PrereqAdmin(admin.ModelAdmin):
    list_display = ('course', 'prereq_course')
    search_fields = ('course__courseName', 'prereq_course__courseName')

@admin.register(Coreq)    
class CoreqAdmin(admin.ModelAdmin):
    list_display = ('course', 'coreq_course')
    search_fields = ('course__courseName', 'coreq_course__courseName')
    
@admin.register(CourseRule)
class CourseRuleAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'linked_course', 'type', 'values')
    search_fields = ('type',)
    list_filter = ('type',)
    
    def linked_course(self , obj):
        link = reverse('admin:course_course_change', args=[obj.course.c_id])
        return format_html('<a href="{}">{}</a>', link, obj.course.course.courseName)
    
    linked_course.short_description = 'Course'