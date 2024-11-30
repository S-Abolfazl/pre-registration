from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CourseCreateApi.as_view(), name='create_course'),
    path('list/', CourseListApi.as_view(), name='list_course'),
    path('list/<pk>', CourseListApi.as_view(), name='course_details'),
    path('update/<pk>', CourseUpdateApi.as_view(), name='update_course'),
    path('createallcourse/', AllCourseCreateApi.as_view(), name='all_course'),
    path('listallcourse/', AllCourseListApi.as_view(), name='list_all_course'),
    path('listallcourse/<pk>', AllCourseListApi.as_view(), name='all_course_details'),
    path('updateallcourse/<pk>', AllCourseUpdateApi.as_view(), name='update_all_course'),
    #path('list/<pk>', UserListApi.as_view(), name='user_details'),
]