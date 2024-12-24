from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Master
from django.views.decorators.csrf import csrf_exempt


