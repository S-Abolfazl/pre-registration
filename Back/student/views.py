from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import EducationalChart
from .serializers import EducationalChartSerializer
from course.models import AllCourses
class EducationalChartCreateApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EducationalChartSerializer(data=request.data)
        if serializer.is_valid():
            chart = serializer.save()
            return Response(
                data={
                    "msg": "ok",
                    "data": f"EducationalChart with id: {chart.chart_id} created successfully",
                    "status":status.HTTP_201_CREATED
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            data={
                "msg": "error",
                "data": serializer.errors,
                "status":status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )
            
class EducationalChartGetApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            year = int(request.data['year'])
            type = request.data['type']
            chart = EducationalChart.objects.get(year=year, type=type)
            serializer = EducationalChartSerializer(chart)
            data = {}
            course_name = None
            for key, value in serializer.data.items():
                if key == "year" or key == "type" or key == "chart_id":
                    data[key] = value
                    continue
                
                try:
                    data[key] = {
                        course_name: {
                            "prereq": list(
                                AllCourses.objects.filter(courseName=course_name)
                                .first()
                                .prereqs_for.values_list("prereq_course__courseName", flat=True)
                            ) if AllCourses.objects.filter(courseName=course_name).exists() else [],
                            "coreq": list(
                                AllCourses.objects.filter(courseName=course_name)
                                .first()
                                .coreqs_for.values_list("coreq_course__courseName", flat=True)
                            ) if AllCourses.objects.filter(courseName=course_name).exists() else [],
                        } 
                        for course_name in value
                    }
                except Exception as e:
                    print(f"Error processing courses in key {key}: {e}")
                    
            return Response(data=data, status=status.HTTP_200_OK)
        except EducationalChart.DoesNotExist:
            return Response(
                data={
                    "msg": "error",
                    "data": f"EducationalChart not found {course_name}",
                    "status":status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )