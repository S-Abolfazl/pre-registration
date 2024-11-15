from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
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
        user = authenticate(username=username, password=password)

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
            


class UserLogoutApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            print("User logged out")
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(data={
                "msg": "ok",
                "data": "Successfully logged out"
            }, status=status.HTTP_200_OK)
        except (TokenError, InvalidToken):
            return Response(data={
                "msg": "error",
                "data": "Invalid token or token already blacklisted"
            }, status=status.HTTP_400_BAD_REQUEST)

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


class UserUpdateApi(APIView):
    permission_classes = [AllowAny]
    def put(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={
                    "msg":"ok",
                    "data":f'user by id:{user.id} updated'
                }, status=status.HTTP_200_OK)
            return Response(
                data={
                    "msg":"error",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"user not found"
            }, status=status.HTTP_404_NOT_FOUND)
            
            
class UserResetPasswordApi(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = User.objects.get(username=request.user.username)
            if request.data["password"] == request.data["confirm_password"]:
                user.set_password(request.data["password"])
                user.save()
                return Response(data={
                    "msg":"ok",
                    "data":"password reset"
                }, status=status.HTTP_200_OK)
            else:
                return Response(data={
                    "msg":"error",
                    "data":"passwords do not match"
                }, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"user not found"
            }, status=status.HTTP_404_NOT_FOUND)