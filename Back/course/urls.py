from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CourseCreateApi.as_view(), name='create_course'),
   # path('list/', UserListApi.as_view(), name='list_user'),
    #path('list/<pk>', UserListApi.as_view(), name='user_details'),
]