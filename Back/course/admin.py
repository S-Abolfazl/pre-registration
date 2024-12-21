from django.contrib import admin
from .models import Course, AllCourses, Prereq, Coreq
from django import forms

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