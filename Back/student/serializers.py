from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    
    def create(self, validated_data):
        m2m_fields = {}
        for field in self.Meta.model._meta.many_to_many:
            if field.name in validated_data:
                m2m_fields[field.name] = validated_data.pop(field.name)
        
        validated_data['type'] = 'student'
        
        student = Student.objects.create(**validated_data)
        
        for field_name, value in m2m_fields.items():
            getattr(student, field_name).set(value)
        
        return student
    