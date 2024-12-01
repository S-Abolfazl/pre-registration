from django.urls import path
from .views import *

urlpatterns = [
    # path('create/', StudentCreateApi.as_view(), name='create_student'),
    path('create/chart/', EducationalChartCreateApi.as_view(), name='create_student'),
]