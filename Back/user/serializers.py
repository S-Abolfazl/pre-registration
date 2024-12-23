import base64
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
            raise serializers.ValidationError("نام کاربری باید بیشتر از 8 کاراکتر باشد.")
        
        if not value.isdigit():
            raise serializers.ValidationError("نام کاربری باید شماره دانشجویی باشد.")
    
        return value
    
    def validate_password(self, value):
        
        if len(value) < 8:
            raise serializers.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد.")
    
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک حرف بزرگ انگلیسی باشد.")
        
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک حرف کوچک انگلیسی باشد.")
        
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک عدد باشد.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک کاراکتر خاص (!@#$%^&*(),.?\":{}|<>) باشد.")
        
        if re.search(r'\s', value):
            raise serializers.ValidationError("رمز عبور نباید شامل فاصله باشد.")
        
        return value
    



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class UserSerializert(serializers.ModelSerializer):

    default_error_messages = {
        'username_required': 'نام کاربری نمی‌تواند خالی باشد.',
        'password_required': 'رمز عبور نمی‌تواند خالی باشد.',
        'email_invalid': 'ایمیل وارد شده معتبر نیست.',
        'type_invalid': 'نوع کاربر باید یکی از مقادیر معتبر باشد.',
        'first_name_required' : 'نام نمیتواند خالی باشد.',
        'last_name_required' : 'نام خانوادگی نمیتواند خالی باشد.',
        'mobile_number_required' : 'شماره موبایل نمیتواند خالی باشد',

    }
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'type', 'first_name', 'last_name',',mobile_number','avatar','avatar_upload']

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
        self.fields['first_name'].error_messages.update({
            'invalid': self.default_error_messages['first_name_required']
        })
        self.fields['last_name'].error_messages.update({
            'invalid': self.default_error_messages['last_name_required']
        })
        self.fields['mobile-number'].error_messages.update({
            'invalid': self.default_error_messages['mobile_number_required']
        })
    def get_avatar(self, obj):
        # نمایش آواتار به صورت Base64
        if obj.avatar:
            return base64.b64encode(obj.avatar).decode('utf-8')
        return None

    def validate_avatar_upload(self, value):
        if value.size > 5 * 1024 * 1024:  # محدودیت حجم به 5MB
            raise serializers.ValidationError("حجم فایل نباید بیشتر از ۵ مگابایت باشد.")
        return value
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user_type = validated_data.get('type', None)
        username = validated_data.get('username', None)
        first_name = validated_data.get('first_naame', None)
        last_name = validated_data.get('last_name', None)
        mobile_number = validated_data.get('mobile_number', None)
        user = super().create(validated_data)
        
        if password:
            user.set_password(password)
            
        if user_type == 'student':
            user.entry_year = int(username[:3])
        elif user_type == 'admin':
            user.is_staff = True
            user.is_superuser = True
        if avatar_upload:
            user.avatar = avatar_upload.read()

        user.first_name = first_name
        user.last_name = last_name
        user.mobile_number = mobile_number
        
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
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
        
        if user_type == 'student':
            user.entry_year = int(username[:3])

        if avatar_upload:
            user.avatar = avatar_upload.read()
        if first_name:
            user.first_name = first_name

        if last_name:
            user.last_name = last_name

        if mobile_number:
            user.mobile_number = mobile_number
        
        user.save()
        return user
    def validate_first_name(self,value):
        if  re.search(r'[A-Z]', value):
            raise serializers.ValidationError("نام نمیتواند شامل حرف انگلیسی باشد.")
        if  re.search(r'[a-z]', value):
            raise serializers.ValidationError("نام نمیتواند شامل حرف انکلیسی باشد.")
        if value.isdigit():
            raise serializers.ValidationError("نام نمیتواند عدد باشد")
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("نام باید فقط شامل حروف باشد.")

    def validate_last_name(self,value):
        if  re.search(r'[A-Z]', value):
            raise serializers.ValidationError("نام خانوداگی نمیتواند شامل حرف انکلیسی باشد.")
        if  re.search(r'[a-z]', value):
            raise serializers.ValidationError("نام خانوداگی نمیتواند شامل حرف انکلیسی باشد.")
        if value.isdigit():
            raise serializers.ValidationError("نام خانوادگی نمیتواند عدد باشد")
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("نام خانوادگی باید فقط شامل حروف باشد.")
    def validate_mobile_number(self,value):
        if not value.isdigit():
            raise serializers.ValidationError("شماره همراه باید عدد باشد")
    def validate_username(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("نام کاربری باید بیشتر از 8 کاراکتر باشد.")
        
        if not value.isdigit():
            raise serializers.ValidationError("نام کاربری باید شماره دانشجویی باشد.")
    
        return value

    
    def validate_password(self, value):
        
        if len(value) < 8:
            raise serializers.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد.")
    
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک حرف بزرگ انگلیسی باشد.")
        
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک حرف کوچک انگلیسی باشد.")
        
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک عدد باشد.")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("رمز عبور باید حداقل شامل یک کاراکتر خاص (!@#$%^&*(),.?\":{}|<>) باشد.")
        
        if re.search(r'\s', value):
            raise serializers.ValidationError("رمز عبور نباید شامل فاصله باشد.")
        
        return value
    
class UserDetailSerializert(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'