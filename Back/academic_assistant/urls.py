from django.urls import path
from .views import *

urlpatterns = [
    path('statistics/bar-chart', StatisticsBarChartApi.as_view(), name='statistics_bar_chart'),
]
