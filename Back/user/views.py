from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer

from django.views.decorators.csrf import csrf_exempt

class UserCreateApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(data={
                "msg":"ok",
                "data":f'user by id:{user.id} created'
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class UserListApi(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk=None):
        try:
            if pk:
                user = User.objects.get(id=pk)
                serializer = UserSerializer(user)
            else:
                users = User.objects.all()
                serializer = UserSerializer(users, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"user not found"
            }, status=status.HTTP_404_NOT_FOUND)

        
class UserDeleteApi(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return Response(data={
                "msg":"ok",
                "data":f'user by id:{pk} deleted'
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"user not found"
            }, status=status.HTTP_404_NOT_FOUND)
        