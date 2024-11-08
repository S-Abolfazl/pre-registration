from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


from .models import User
from .serializers import UserSerializer

from django.views.decorators.csrf import csrf_exempt

class UserSignupApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            return Response(data={
                "msg":"ok",
                "data":{
                    "user": serializer.data,
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class UserListApi(APIView):
    permission_classes = [IsAuthenticated]
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

class UserLoginApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            return Response(data={
                "msg": "ok",
                "data": {
                    "user": UserSerializer(user).data,
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={
                "msg": "error",
                "data": "Invalid username or password"
            }, status=status.HTTP_401_UNAUTHORIZED)