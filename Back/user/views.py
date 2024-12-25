from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from social_django.utils import load_strategy
from social_core.backends.google import GoogleOAuth2

from .models import User
from .serializers import UserSerializer, UserDetailSerializer, UserUpdateSerializer
from user.permissions import IsStudent
class UserSignupApi(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary="User Signup",
        operation_description="Endpoint to create a new user and return tokens.",
        request_body=UserSerializer,
    )
    
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
                    "refresh_token": refresh_token,
                    "status": status.HTTP_201_CREATED
                }
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class UserListApi(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(
        operation_summary="User List",
        operation_description="Endpoint to retrieve all users.",
    )
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserDetailSerializer(users, many=True)
        return Response(data={
            "msg":"ok",
            "data":serializer.data,
            "status":status.HTTP_200_OK           
            }
            , status=status.HTTP_200_OK)
    
class UserDetailApi(APIView):
    permission_classes = [IsAuthenticated, IsStudent]
    
    @swagger_auto_schema(
        operation_summary="User Detail",
        operation_description="Endpoint to retrieve a user by id.",
    )
    
    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(data={
                "msg": "ok",
                "data": serializer.data,
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

class UserLoginApi(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary="User Login",
        operation_description="Endpoint to login a user and return tokens.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password')
            }
        )
    )

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
                    "refresh_token": refresh_token,
                    "status": status.HTTP_200_OK
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={
                "msg": "error",
                "data": "نام کاربری یا رمز عبور اشتباه است",
                "status": status.HTTP_401_UNAUTHORIZED
            }, status=status.HTTP_401_UNAUTHORIZED)
            


class UserLogoutApi(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="User Logout",
        operation_description="Endpoint to logout a user and blacklist the refresh token.",
        # security=[{'Bearer': []}],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['refresh_token'],
            properties={
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh Token')
            }
        )
    )
    def post(self, request):
        try:
            print("User logged out")
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(data={
                "msg": "ok",
                "data": "با موفقیت خارج شدید",
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except (TokenError, InvalidToken):
            return Response(data={
                "msg": "error",
                "data": "توکن نامعتبر است یا قبلاً غیرفعال شده است",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)

class UserDeleteApi(APIView):
    permission_classes = [AllowAny, IsAdminUser]
    
    @swagger_auto_schema(
        operation_summary="User Delete",
        operation_description="Endpoint to delete a user by id.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['id'],
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID')
            }
        )
    )
    
    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return Response(data={
                "msg":"ok",
                "data":f'user by id:{pk} deleted',
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"user not found",
                "status": status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={
                "msg":"error",
                "data":str(e),
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateApi(APIView):
    permission_classes = [IsStudent, IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="User Patch",
        operation_description="Endpoint to partially update a user by id, including uploading an avatar.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'type': openapi.Schema(type=openapi.TYPE_STRING, description='Type'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
                'mobile_number': openapi.Schema(type=openapi.TYPE_STRING, description='Mobile number'),
                'avatar': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="binary",
                    description="Upload an avatar image"
                )
            },
        )
    )
    def patch(self, request):
        try:
            user = request.user
            serializer = UserUpdateSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data={
                    "msg": "ok",
                    "data": f'کاربر با نام کاربری {user.username} به روز شد',
                    "status": status.HTTP_200_OK
                }, status=status.HTTP_200_OK)
            return Response(
                data={
                    "msg": "error",
                    "data": serializer.errors,
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(data={
                "msg": "error",
                "data": "کاربر یافت نشد",
                "status": status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={
                "msg": "error",
                "data": 'در پردازش اطلاعات مشکلی پیش آمده است',
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
            
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
                    "data":"password reset",
                    "status": status.HTTP_200_OK
                }, status=status.HTTP_200_OK)
            else:
                return Response(data={
                    "msg":"error",
                    "data":"passwords do not match",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(data={
                "msg":"error",
                "data":"user not found",
                "status": status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
            
            
class GoogleLoginApi(APIView):
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema(
        operation_summary="Google Login",
        operation_description="Endpoint to login a user using a Google token.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['token'],
            properties={
                'token': openapi.Schema(type=openapi.TYPE_STRING, description='Google Token')
            }
        )
    )
    
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response(data={
                    "msg":"error",
                    "data":"Token is required",
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status= status.HTTP_400_BAD_REQUEST          
            )
            
        try:
            strategy = load_strategy(request)
            backend = GoogleOAuth2(strategy=strategy)
            user_info = backend.user_data(token)
            
            email = user_info.get('email')
            if not email:
                return Response(data={
                    "msg":"error",
                    "data":"Email not found in token",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)
                
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(data={
                    "msg": "error", 
                    "data": "کاربری با این ایمیل یافت نشد", 
                    "status": status.HTTP_401_UNAUTHORIZED   
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
                
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            return Response({
                "msg": "ok",
                "data": {
                    "user": {"id": user.id, "email": user.email, "username": user.username},
                    "access_token": access_token,
                    "refresh_token": refresh_token
                },
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={
                    "msg": "error", 
                    "data": "مشکلی در پردازش اطلاعات پیش آمده است", 
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )