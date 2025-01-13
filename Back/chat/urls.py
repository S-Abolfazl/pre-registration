from django.urls import path

from .views import *

urlpatterns = [
    path('list/', ChatListAPIView.as_view(), name='chats'),
    path('detail/<pk>/', ChatListAPIView.as_view(), name='chat'),
    path('create/', ChatCreateAPIView.as_view(), name='create_chat'),
    path('delete/<pk>/', ChatDeleteAPIView.as_view(), name='delete_chat'),

    path('get_messages/', MessageListAPIView.as_view(), name='get-msgs'),
    path('create_message/', MessageCreateAPIView.as_view(), name='create-msg'),
    path('update_message/<pk>/', MessageUpdateAPIView.as_view(), name='update-msg'),
    path('delete_message/<pk>/', MessageDeleteAPIView.as_view(), name='delete-msg'),
]
