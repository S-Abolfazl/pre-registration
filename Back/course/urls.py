from django.urls import path
from .views import *
from .views import CourseCreateApi
urlpatterns = [
    path('create/', CourseCreateApi.as_view(), name='create_course'),
    path('list/', CourseListApi.as_view(), name='list_course'),
    path('list/<pk>', CourseListApi.as_view(), name='course_details'),
    path('update/<pk>', CourseUpdateApi.as_view(), name='update_course'),
    #path('list/<pk>', UserListApi.as_view(), name='user_details'),
]