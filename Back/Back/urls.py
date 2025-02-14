"""
URL configuration for Back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Detailed documentation for all API endpoints.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('course/', include('course.urls')),
    path('student/', include('student.urls')),
    path('chat/', include('chat.urls')),
    path('registration-form/', include('registrationForm.urls')),
    path('academic-assistant/', include('academic_assistant.urls')),
    path('master/', include('master.urls')),
    path('notification/', include('notification.urls')),
        
    # swagger
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)