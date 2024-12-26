from rest_framework import serializers
from .models import Master
from django.core.files.base import ContentFile
import os

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'  # همه فیلدهای مدل را در API پوشش می‌دهد


class MasterUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required = False, allow_null = True)
    model = Master
    fields = '__all__' #

def update(self, instance, validate_data):
    avatar_upload = validate_data.pop('avatar', None)
    if avatar_upload:
            if Master.avatar:
                old_avatar_path = Master.avatar.path
                if os.path.exists(old_avatar_path):
                    os.remove(old_avatar_path)
                    
            ext = os.path.splitext(avatar_upload.name)[1]
            new_filename = f"{Master.id}{ext}"
            Master.avatar.save(new_filename, ContentFile(avatar_upload.read()), save=False)
    Master.save()
    return Master