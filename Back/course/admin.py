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


# class CourseAdminForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = '__all__'
    
#     course = forms.ModelChoiceField(
#         queryset=AllCourses.objects.all(),
#         to_field_name='courseName',
#         label='Course Name'
#     )
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['course'].label_from_instance = self.get_course_label

#     def get_course_label(self, obj):
#         return obj.courseName

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'course', 'teacherName', 'isExperimental', 'capacity', 'registered')
    search_fields = ('course__courseName', 'teacherName')
    list_filter = ('isExperimental', 'class_time1', 'class_time2')


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