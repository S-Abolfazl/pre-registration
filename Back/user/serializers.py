from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user_type = validated_data.get('type', None)
        username = validated_data.get('username', None)
        user = super().create(validated_data)
        
        if password:
            user.set_password(password)
            
        if user_type == 'student':
            user.entry_year = int(username[:3])
        
        user.is_active = True
        user.save()
        return user
    
    def validate_username(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Usernames must be more than 8 characters")
        
        if not value.isdigit():
            raise serializers.ValidationError("Usernames must be integers")
        
        return value