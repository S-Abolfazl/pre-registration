from django.contrib import admin
from .models import CompletedCourses, EducationalChart


@admin.register(CompletedCourses)
class CompletedCoursesAdmin(admin.ModelAdmin):
    list_display = ('complete_course_id', 'student', 'course')
    search_fields = ('student__username', 'course__courseName')
    list_filter = ('student',)

@admin.register(EducationalChart)
class EducationalChartAdmin(admin.ModelAdmin):
    list_display = ('chart_id', 'year', 'type')
    search_fields = ('year', 'type')
    list_filter = ('year','type')