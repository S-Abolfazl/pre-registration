from rest_framework.permissions import BasePermission
from .models import User

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        
        is_student = False
        try:
            user = User.objects.get(id=request.user.id)
            is_student = user.type == 'student'
        except User.DoesNotExist:
            is_student = False
        
        return is_student
    
class IsAcademicAssistant(BasePermission):
    def has_permission(self, request, view):
        
        is_academic_assistant = False
        try:
            user = User.objects.get(id=request.user.id)
            is_academic_assistant = user.type == 'academicassistant'
        except User.DoesNotExist:
            is_academic_assistant = False
        
        return is_academic_assistant
    
class IsSupport(BasePermission):
    def has_permission(self, request, view):
        
        is_support = False
        try:
            user = User.objects.get(id=request.user.id)
            is_support = user.type == 'support'
        except User.DoesNotExist:
            is_support = False
        
        return is_support