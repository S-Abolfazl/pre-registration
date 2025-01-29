from django.urls import path
from .views import *

urlpatterns = [
    path('', NotificationApi.as_view(), name='notification'),
]
