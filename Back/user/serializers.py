from rest_framework import serializers
import re
from .models import User

class UserSerializer(serializers.ModelSerializer):

    default_error_messages = {
        'username_required': 'نام کاربری نمی‌تواند خالی باشد.',
        'password_required': 'رمز عبور نمی‌تواند خالی باشد.',
        'email_invalid': 'ایمیل وارد شده معتبر نیست.',
        'type_invalid': 'نوع کاربر باید یکی از مقادیر معتبر باشد.',
    }
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'type']

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
            'invalid': self.default_error_messages['email_invalid']
        })
        self.fields['type'].error_messages.update({
            'invalid_choice': self.default_error_messages['type_invalid']
        })
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user_type = validated_data.get('type', None)
        username = validated_data.get('username', None)
        user = super().create(validated_data)
        
        if password:
            user.set_password(password)
            
        if user_type == 'student':
            user.entry_year = int(username[:3])
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
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
        
        if user_type == 'student':
            user.entry_year = int(username[:3])
        
        user.save()
        return user
    
    def validate_username(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Usernames must be more than 8 characters")
        
        if not value.isdigit():
            raise serializers.ValidationError("Usernames must be integers")
        
        return value
    
    def validate_password(self, value):
        
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must include at least one uppercase letter.")
        
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Password must include at least one lowercase letter.")
        
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("Password must include at least one digit.")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("Password must include at least one special character (!@#$%^&*(),.?\":{}|<>).")
        
        if re.search(r'\s', value):
            raise serializers.ValidationError("Password must not contain any spaces.")
        
        return value