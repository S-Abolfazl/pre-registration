from django.urls import path
from .views import *

urlpatterns = [
    path('create/', UserCreateApi.as_view(), name='create_user'),
    path('list/', UserListApi.as_view(), name='list_user'),
    path('list/<pk>', UserListApi.as_view(), name='user_derails'),
    path('update/<pk>', UserUpdateApi.as_view(), name='update_user'),
]

