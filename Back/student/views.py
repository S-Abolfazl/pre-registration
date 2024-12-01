from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import EducationalChart
from .serializers import EducationalChartSerializer


class EducationalChartCreateApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = EducationalChartSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            educationalChart = serializer.save()
            return Response(data={
                "msg":"ok",
                "data":f'educational chart by id:{educationalChart.chart_id} created',
                "status": status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            data={
                "msg":"error",
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )