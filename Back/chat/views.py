from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from user.models import User

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ChatListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get all chats",
        operation_description="Get all chats to show for user",
        responses={
            200: openapi.Response("ok", ChatSerializer),
            404: "Chat not found",
        },
    )
    
    def get(self, request, pk=None):
        user = request.user

        if user.type == "support":
            chats = Chat.objects.all()
            serializer = ChatSerializer(chats, many=True)
        else:
            if pk:
                try:
                    chat = Chat.objects.get(id=pk)
                    serializer = ChatSerializer(chat)
                except Chat.DoesNotExist:
                    return Response({
                        "msg": "error",
                        "data": "Chat not found",
                        "status": status.HTTP_404_NOT_FOUND,
                    }, status=status.HTTP_404_NOT_FOUND)
            else:
                chats = Chat.objects.all()
                serializer = ChatSerializer(chats, many=True)

        return Response({
            "msg": "ok",
            "data": serializer.data,
            "status": status.HTTP_200_OK,
        }, status=status.HTTP_200_OK)


class ChatCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Create chat",
        operation_description="create a chat between user and supporter",
        responses={
            201: "Chat created successfully",
            400: "Chat not created",
        },
    )

    def post(self, request):
        sender = request.user
        receiver = User.objects.filter(type='support').first()
        if not receiver:
            return Response({
                "msg": "error",
                "data": "support does not exist",
                "status": status.HTTP_400_BAD_REQUEST,
            }, status=status.HTTP_400_BAD_REQUEST)

        chat, created = Chat.objects.get_or_create(sender=sender, receiver=receiver)
        serializer = ChatSerializer(chat)
        return Response({
            "msg": "ok",
            "data": serializer.data,
            "status": status.HTTP_200_OK,
        }, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


class ChatDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Delete chat",
        operation_description="api for deleting a chat",
        responses={
            200: "Chat deleted successfully",
            400: "Chat not deleted",
        },
    )
    
    def delete(self, request, pk):
        try:
            Chat.objects.get(pk=pk).delete()
            return Response({
                "msg": "ok",
                "data": "deleted success",
                "status": status.HTTP_200_OK,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "msg": "error",
                "data": str(e),
                "status": status.HTTP_400_BAD_REQUEST,
            }, status=status.HTTP_400_BAD_REQUEST)


class MessageListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary = "List messages",
        operation_description="displays a list of messages",
        responses={
            200: openapi.Response("ok", MessageSerializer),
            400: "there is no message",
        }
    )
    
    def post(self, request):
        try:
            chat_id = Chat.objects.get(id=request.data.get('chat_id')).id
        except Exception:
            Response({
                "msg": "error",
                "data": "چت وجود ندارد",
                "status": status.HTTP_400_BAD_REQUEST,
            }, status=status.HTTP_400_BAD_REQUEST)

        msgs = Message.objects.filter(chat=chat_id)
        serializer = MessageSerializer(msgs, many=True)

        return Response({
                "msg": "ok",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }, status=status.HTTP_200_OK)


class MessageCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()

        try:
            data['sender'] = User.objects.get(id=data['sender'])
            data['receiver'] = User.objects.get(id=data['receiver'])
        except Exception as e:
            return Response({
                "msg": "فرستنده یا گیرنده نامعتبر است",
                "data": "",
                "status": status.HTTP_400_BAD_REQUEST,
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            msg = serializer.save()

            return Response({
                "msg": "با موفقیت ارسال شد",
                "data": {
                    "id": msg.id,
                    "content": msg.content,
                    "created": msg.created,
                    "updated": msg.updated,
                },
                "status": status.HTTP_200_OK,
            }, status=status.HTTP_200_OK)

        return Response({
            "msg": "خطا در ارسال پیام",
            "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST,
        }, status=status.HTTP_400_BAD_REQUEST)


class MessageUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        try:
            message = Message.objects.get(id=pk)
        except Message.DoesNotExist:
            return Response({
                "msg": "پیام یافت نشد",
                "data": "",
                "status": status.HTTP_404_NOT_FOUND,
            }, status=status.HTTP_404_NOT_FOUND)

        # Update the object
        serializer = MessageSerializer(message, data=request.data, partial=False)

        if serializer.is_valid():
            updated_message = serializer.save()

            return Response({
                "msg": "پیام با موفقیت به‌روزرسانی شد",
                "data": {
                    "id": updated_message.id,
                    "content": updated_message.content,
                    "created": updated_message.created,
                    "updated": updated_message.updated,
                },
                "status": status.HTTP_200_OK,
            }, status=status.HTTP_200_OK)

        return Response({
            "msg": "خطا در به‌روزرسانی پیام",
            "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST,
        }, status=status.HTTP_400_BAD_REQUEST)


class MessageDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        try:
            message = Message.objects.get(id=pk)
        except Message.DoesNotExist:
            return Response({
                "msg": "پیام یافت نشد",
                "data": "",
                "status": status.HTTP_404_NOT_FOUND,
            }, status=status.HTTP_404_NOT_FOUND)

        message.delete()

        return Response({
            "msg": "پیام با موفقیت حذف شد",
            "data": "",
            "status": status.HTTP_204_NO_CONTENT,
        }, status=status.HTTP_204_NO_CONTENT)
