from django.urls import path
from .views import *

urlpatterns = [
    path('statistics/bar-chart', StatisticsBarChartApi.as_view(), name='statistics_bar_chart'),
    path('statistics/participation-percent', StatisticsParticipationPercentApi.as_view(), name='statistics_participation_percent'),
    path('statistics/overflowed-courses', StatisticsOwerFlowedCoursesApi.as_view(), name='statistics_overflowed_courses'),
]
