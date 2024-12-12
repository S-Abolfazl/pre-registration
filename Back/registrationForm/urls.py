from django.urls import path
from .views import *

urlpatterns = [
    path('list/', RegistrationFormListView.as_view(), name='registration_form_list'),
    path('create/', RegistrationFormCreateView.as_view(), name='registration_form_create'),
    path('<uuid:form_id>/', RegistrationFormListView.as_view(), name='registration_form_detail'),
    path('update/<uuid:form_id>/', RegistrationFormUpdateView.as_view(),
         name='registration_form_update'),
    path('delete/<uuid:form_id>/', RegistrationFormDeleteView.as_view(),
         name='registration_form_delete'),

     path('courses-data/', RegistrationFormDataApi.as_view(), name='registration_form_data'),
     path('confrim/', RegistrationFormConfirmApi.as_view(), name='registration_form_confirm'),
]
