from django.contrib import admin
from .models import RegistrationForm, SelectedCourse

@admin.register(RegistrationForm)
class RegistrationFormAdmin(admin.ModelAdmin):
    list_display = ('form_id', 'student_id', 'creationDateTime', 'lastUpdate_DateTime')
    search_fields = ('student_id', 'student_id__username')
    list_filter = ('creationDateTime',)
    readonly_fields = ('form_id', 'creationDateTime', 'lastUpdate_DateTime')

@admin.register(SelectedCourse)
class SelectedCourseAdmin(admin.ModelAdmin):
    list_display = ('form', 'course', 'course_name')
    search_fields = ('form__form_id','course__course__courseName')

    def course_name(self, obj):
        return obj.course.course.courseName
    
    course_name.short_description = 'Course Name'