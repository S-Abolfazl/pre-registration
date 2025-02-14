from rest_framework import serializers
import re
from .models import User
import os
from django.core.files.base import ContentFile

class UserSerializer(serializers.ModelSerializer):

    default_error_messages = {
        'username_required': 'نام کاربری نمی‌تواند خالی باشد',
        'password_required': 'رمز عبور نمی‌تواند خالی باشد',
        'email_required': 'ایمیل نمی‌تواند خالی باشد',
        'email_invalid': 'ایمیل وارد شده معتبر نیست',
        'type_required': 'نوع کاربر نمی‌تواند خالی باشد',
        'type_invalid': 'نوع کاربر باید یکی از مقادیر معتبر باشد',
        'username_exists': 'کاربری با این نام کاربری از قبل وجود دارد',
        'email_exists': 'کاربری با این ایمیل از قبل وجود دارد',
        'first_name_required': 'نام نمی‌تواند خالی باشد',
        'last_name_required': 'نام خانوادگی نمی‌تواند خالی باشد',
        'mobile_number_required': 'شماره موبایل نمی‌تواند خالی باشد',
        'first_name_blank': 'نام نمی‌تواند خالی باشد',
        'last_name_blank': 'نام خانوادگی نمی‌تواند خالی باشد',
        'mobile_number_blank': 'شماره موبایل نمی‌تواند خالی باشد',
    }
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'type', 'first_name', 'last_name', 'mobile_number', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # تنظیم پیام‌های خطا برای هر فیلد
        self.fields['username'].error_messages.update({
            'required': self.default_error_messages['username_required'],
            'blank': self.default_error_messages['username_required']
        })
        self.fields['password'].error_messages.update({
            'required': self.default_error_messages['password_required'],
            'blank': self.default_error_messages['password_required']
        })
        self.fields['email'].error_messages.update({
            'required': self.default_error_messages['email_required'],
            'blank': self.default_error_messages['email_required'],
            'invalid': self.default_error_messages['email_invalid']
        })
        self.fields['type'].error_messages.update({
            'required': self.default_error_messages['type_required'],
            'blank': self.default_error_messages['type_required'],
            'invalid_choice': self.default_error_messages['type_invalid']
        })
        self.fields['first_name'].error_messages.update({
            'required': self.default_error_messages['first_name_required'],
            'blank': self.default_error_messages['first_name_blank']
        })
        self.fields['last_name'].error_messages.update({
            'required': self.default_error_messages['last_name_required'],
            'blank': self.default_error_messages['last_name_blank']
        })
        self.fields['mobile_number'].error_messages.update({
            'required': self.default_error_messages['mobile_number_required'],
            'blank': self.default_error_messages['mobile_number_blank']
        })
        
    def validate(self, data):
        username = data.get('username')
        user_type = data.get('type')
        if username:
            if len(username) < 8:
                raise serializers.ValidationError("نام کاربری باید بیشتر از 8 کاراکتر باشد")
            
            if not username.isdigit():
                if user_type == "student":
                    raise serializers.ValidationError("نام کاربری باید شماره دانشجویی باشد")
                else:
                    raise serializers.ValidationError("نام کاربری باید فقط شامل اعداد باشد")
            
            if username[0] != '4' and username[0] != '9' and user_type == "student":
                raise serializers.ValidationError("شماره دانشجویی معتبر نیست")
        
        return data
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user_type = validated_data.get('type', None)
        username = validated_data.get('username', None)
        user = super().create(validated_data)
        
        if password:
            user.set_password(password)
            
        if user_type == 'student':
            if username[0] == '4':
                user.entry_year = int(username[:3])
            elif username[0] == '9': 
                user.entry_year = int(username[:2])
        elif user_type == 'admin':
            user.is_staff = True
            user.is_superuser = True
        
        user.is_active = True
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user_type = validated_data.get('type', None)
        username = validated_data.get('username', None)
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)
        mobile_number = validated_data.get('mobile_number', None)
        avatar_upload = validated_data.pop('avatar', None)
        user = super().update(instance, validated_data)
        
        if username:
            user.username = username
        
        if password:
            user.set_password(password)
        
        if user_type:
            user.type = user_type
        
        if user_type == 'student':
            if username[0] == '4':
                user.entry_year = int(username[:3])
            elif username[0] == '9': 
                user.entry_year = int(username[:2])
            
        if avatar_upload:
            if user.avatar:
                old_avatar_path = user.avatar.path
                if os.path.exists(old_avatar_path):
                    os.remove(old_avatar_path)
                    
            ext = os.path.splitext(avatar_upload.name)[1]
            new_filename = f"{user.id}{ext}"
            user.avatar.save(new_filename, ContentFile(avatar_upload.read()), save=False)
                
        if first_name:
            user.first_name = first_name

        if last_name:
            user.last_name = last_name

        if mobile_number:
            user.mobile_number = mobile_number
        
        user.save()
        return user

    
    def validate_password(self, value):
        
        if len(value) < 8:
            raise serializers.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد")
    
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک حرف بزرگ انگلیسی باشد")
        
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک حرف کوچک انگلیسی باشد")
        
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک عدد باشد")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک کاراکتر خاص (!@#$%^&*(),.?\":{}|<>) باشد")
        
        if re.search(r'\s', value):
            raise serializers.ValidationError("رمز عبور نباید شامل فاصله باشد")
        
        return value
    
    def validate_first_name(self, value):
        if not re.fullmatch(r'^[\u0600-\u06FF\s]+$', value):
            raise serializers.ValidationError("نام باید فقط شامل حروف فارسی باشد")
        return value

    def validate_last_name(self, value):
        if not re.fullmatch(r'^[\u0600-\u06FF\s]+$', value):
            raise serializers.ValidationError("نام خانوادگی باید فقط شامل حروف فارسی باشد")
        return value

    def validate_mobile_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("شماره همراه باید عدد باشد")
        if len(value) != 11:
            raise serializers.ValidationError("شماره همراه باید 11 رقم باشد")
        return value
    



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
class UserDetailSerializert(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'