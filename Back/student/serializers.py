from rest_framework import serializers

from .models import EducationalChart

class EducationalChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalChart
        fields = '__all__' 