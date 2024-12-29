from django.urls import path
from .views import *

urlpatterns = [
    path('list/', UserListApi.as_view(), name='list_user'),
    path('detail/', UserDetailApi.as_view(), name='user_derails'),
    path('delete/<pk>', UserDeleteApi.as_view(), name='delete_user'),
    path('signup/', UserSignupApi.as_view(), name='signup_user'),
    path('login/', UserLoginApi.as_view(), name='login_user'),
    path('logout/', UserLogoutApi.as_view(), name='logout_user'),
    path('update/', UserUpdateApi.as_view(), name='update_user'),
    path('forgot-password/', UserForgotPasswordApi.as_view(), name='reset_password_user'),
    path('login-google/', GoogleLoginApi.as_view(), name='login_google_user'),
    path('refresh-token/', RefreshTokenApi.as_view(), name='refresh_token_user'),
]

