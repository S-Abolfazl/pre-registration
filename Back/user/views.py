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
from rest_framework import serializers

from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from user.permissions import IsStudent
class UserSignupApi(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary="User Signup",
        operation_description="Endpoint to create a new user and return tokens.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password', 'email', 'type'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'type': openapi.Schema(type=openapi.TYPE_STRING, description='Type'),
            }
        )
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
            
            serializer = UserSerializer(user)
            user_data = {}
            user_data = {
                key: value
                for key, value in serializer.data.items()
                if key not in ['password', 'first_name', 'last_name', 'mobile_number', 'avatar']
            }
            return Response(data={
                "msg": "ok",
                "data": {
                    "user": user_data,
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
            
    
class RefreshTokenApi(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Refresh Token",
        operation_description="Endpoint to refresh an access token using a refresh token.",
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
            refresh_token = request.data["refresh_token"]
            if not refresh_token:
                return Response(data={
                    "msg": "error",
                    "data": "رفرش توکن مورد نیاز است",
                    "status": status.HTTP_400_BAD_REQUEST
                })
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
            return Response(data={
                "msg": "ok",
                "data": {
                    "access_token": access_token,
                    "status": status.HTTP_200_OK
                }
            }, status=status.HTTP_200_OK)
        except (TokenError, InvalidToken):
            return Response(data={
                "msg": "error",
                "data": "توکن نامعتبر است یا قبلاً غیرفعال شده است",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
            


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
            serializer = UserSerializer(user, data=request.data, partial=True)
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

            
        
class UserForgotPasswordApi(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_summary="Forgot Password",
        operation_description="Endpoint to reset a user's password.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password', 'confirm_password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, description='Confirm Password')
            }
        )
    )
    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            confirm_password = request.data.get("confirm_password")
            
            user = User.objects.get(email=email)
            
            if password != confirm_password:
                return Response(data={
                    "msg": "error",
                    "data": "کلمه عبور و تکرار آن باید یکسان باشند",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = UserSerializer()
            try:
                validated_password = serializer.validate_password(password)
            except serializers.ValidationError as e:
                return Response(data={
                    "msg": "error",
                    "data": e.detail,
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(validated_password)
            user.save()
            
            return Response(data={
                "msg": "ok",
                "data": "کلمه عبور با موفقیت تغییر یافت",
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(data={
                "msg": "error",
                "data": "User not found",
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

    def get(self, request):
        # Retrieve the authorization code from query parameters
        code = request.query_params.get('code')
        if not code:
            return Response(
                {"msg": "error", "data": "Authorization code is required", "status": status.HTTP_400_BAD_REQUEST},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Load the strategy and backend
            strategy = load_strategy(request)
            backend = GoogleOAuth2(strategy=strategy)

            # Exchange the code for a token
            token_info = backend.request_access_token(code)
            token = token_info.get("access_token")

            # Retrieve user information
            user_info = backend.user_data(token)
            email = user_info.get("email")

            if not email:
                return Response(
                    {"msg": "error", "data": "Email not found in token", "status": status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Check if the user exists
            from django.contrib.auth.models import User
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(
                    {"msg": "error", "data": "کاربری با این ایمیل یافت نشد", "status": status.HTTP_401_UNAUTHORIZED},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Redirect to frontend with tokens
            frontend_redirect_url = f"http://127.0.0.1:3000/panel?access_token={access_token}&refresh_token={refresh_token}"
            return redirect(frontend_redirect_url)

        except Exception as e:
            return Response(
                {"msg": "error", "data": "مشکلی در پردازش اطلاعات پیش آمده است", "status": status.HTTP_500_INTERNAL_SERVER_ERROR},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )