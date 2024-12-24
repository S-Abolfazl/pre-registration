from rest_framework import serializers
from .models import Master

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'  # همه فیلدهای مدل را در API پوشش می‌دهد
