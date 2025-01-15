from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class NotificationApi(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get all notifications",
        operation_description="Get all notifications to show for user",
    )
    def get(self, request):
        notifications = Notification.objects.all()
        return Response(
            data={
                "msg" : "ok",
                "data" : [
                    {
                        "title" : notification.title,
                        "content" : notification.content,
                        "created_at" : notification.created_at
                    } for notification in notifications
                ],
                "status" : status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )