from django.urls import path
from .views import *

urlpatterns = [
    # path('create/', StudentCreateApi.as_view(), name='create_student'),
    path('chart/create/', EducationalChartCreateApi.as_view(), name='create_chart'),
    path('chart/', EducationalChartGetApi.as_view(), name='get_chart'),
    path('selecet-passed-course/',AddCompletedCourseApi.as_view(), name='selecetpassed_Course'),
    path('courses/', CoursesForPassedCoursesApi.as_view(), name='get_courses'),
]