from django.urls import path
from .views import *
urlpatterns = [
    path('create/', MasterCreateApi.as_view(), name = 'create_master'),
    path('delete/', MasterDeleteApi.as_view(), name = 'delete_master'),
    path('update/', MasterUpdateApi.as_view(), name = 'update_master'),
    path('list/', MasterListApi.as_view(), name = 'list_master'),
]