from django.urls import path
from .views import *

urlpatterns = [
    path('list/', UserListApi.as_view(), name='list_user'),
    path('list/<pk>', UserListApi.as_view(), name='user_derails'),
    path('signup/', UserSignupApi.as_view(), name='signup_user'),
    path('login/', UserLoginApi.as_view(), name='login_user'),
]

