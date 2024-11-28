from rest_framework import BasePermissions
from .models import User

class IsStudent(BasePermissions):
    def has_permission(self, request, view):
        
        is_student = False
        try:
            user = User.objects.get(id=request.user.id)
            is_student = user.type == 'student'
        except User.DoesNotExist:
            is_student = False
        
        return is_student