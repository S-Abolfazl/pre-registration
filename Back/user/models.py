from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    
    USER_TYPE={
        ('student', 'student'),
        ('academicassistant', 'academicassistant'),
        ('admin', 'admin'),
        ('support', 'support'),
    }
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    username = models.CharField(unique=True,max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    type = models.CharField(max_length=30, choices=USER_TYPE)
    entry_year = models.IntegerField(null=True)
    
    class Meta:
        db_table = "User"
    
    def __str__(self) -> str:
        return self.username
    
class AccessLevel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    title = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = "AccessLevel"
        
    def __str__(self) -> str:
        return self.title
    
class UserAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_level = models.ForeignKey(AccessLevel, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "UserAccess"
        unique_together = (('user', 'access_level'),)
        
    def __str__(self) -> str:
        return f"{self.user} - {self.access_level}"