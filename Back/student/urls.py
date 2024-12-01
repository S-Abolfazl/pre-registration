from django.urls import path
from .views import *

urlpatterns = [
    # path('create/', StudentCreateApi.as_view(), name='create_student'),
    path('chart/create/', EducationalChartCreateApi.as_view(), name='create_chart'),
    path('chart/list/', EducationalChartListApi.as_view(), name='list_chart'),
    path('chart/list/<pk>/', EducationalChartListApi.as_view(), name='list_chart_by_id'),
]