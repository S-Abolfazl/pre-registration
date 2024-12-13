from django.urls import path
from .views import *

urlpatterns = [
    path('create-courses-in-term/', CourseCreateApi.as_view(), name='create_courses_in_term'),
    path('list-courses-in-term/', CourseListApi.as_view(), name='list_courses_in_term'),
    path('list-courses-in-term/<pk>', CourseListApi.as_view(), name='course_in_term_details'),
    path('update-course-in-term/<pk>', CourseUpdateApi.as_view(), name='update_course'),
    path('delete-course-in-term/<pk>', CourseDeleteApi.as_view(), name='delete_course'),
    path('create/', AllCourseCreateApi.as_view(), name='all_course'),
    path('list/', AllCourseListApi.as_view(), name='list_all_course'),
    path('list/<pk>', AllCourseListApi.as_view(), name='all_course_details'),
    path('update/<pk>', AllCourseUpdateApi.as_view(), name='update_all_course'),
    path('delete/<pk>', AllCourseDeleteApi.as_view(), name='delete_all_course'),
    path('courses-in-term/data', CourseinTermApi.as_view(), name='course_in_term_data'),
    #path('list/<pk>', UserListApi.as_view(), name='user_details'),
]