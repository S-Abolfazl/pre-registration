from rest_framework import serializers

from .models import EducationalChart

class EducationalChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalChart
        fields = '__all__'
    
    def create(self, validated_data):
        image_file = self.context['request'].FILES.get('image')
        print(image_file)
        educational_chart = EducationalChart(
            year=validated_data.get('year'),
            type=validated_data.get('type')
        )
        
        if image_file:
            educational_chart.save_image(image_file)
        
        educational_chart.save()
        return educational_chart