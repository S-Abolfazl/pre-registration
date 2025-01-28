from rest_framework import serializers
from .models import Master
from django.core.files.base import ContentFile
import os

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'  # همه فیلدهای مدل را در API پوشش می‌دهد


class MasterUpdateSerializer(serializers.ModelSerializer):
    #avatar = serializers.ImageField(required = False, allow_null = True)
    model = Master
    fields = '__all__' #

def update(self, instance, validate_data):
    avatar_upload = validate_data.pop('avatar', None)
    name = validate_data.pop('name', None)
    education = validate_data.pop('education', None)
    specialization = validate_data.pop('specializatioin', None)
    description = validate_data.pop('description', None)
    department = validate_data.pop('department', None)
    mobile_number = validate_data.pop('mobile_number', None)
    email = validate_data.pop('email', None)
    field = validate_data.pop('field', None)
    rate = validate_data.pop('rate', None)
    master = super().update(instance, validate_data)
    

    if name:
         master.name = name
    
    if education:
         master.education = education
    if specialization:
         master.specialization = specialization
    if description:
         master.description = description
    if department:
         master.department = department
    if mobile_number:
         master.mobile_number = mobile_number
    if email:
         master.email = email
    if field:
         master.field = field
    if rate:
         master.rate = rate
         
    
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