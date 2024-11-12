from django.urls import path
from .views import *

urlpatterns = [
    path('list/', UserListApi.as_view(), name='list_user'),
    path('list/<pk>', UserListApi.as_view(), name='user_derails'),
    path('delete/<pk>', UserDeleteApi.as_view(), name='delete_user'),
    path('signup/', UserSignupApi.as_view(), name='signup_user'),
    path('login/', UserLoginApi.as_view(), name='login_user'),
    path('logout/', UserLogoutApi.as_view(), name='logout_user'),
    path('update/<pk>', UserUpdateApi.as_view(), name='update_user'),
]

