from django.urls import path
from .views import *

urlpatterns = [
    # path('create/', StudentCreateApi.as_view(), name='create_student'),
    path('chart/get/', EducationalChartGetApi.as_view(), name='get_student'),
]