from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated


from .serializers import StudentSerializer


class StudentCreateApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            return Response(data={
                "msg":"ok",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )