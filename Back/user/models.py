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
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=30, choices=USER_TYPE)
    entry_year = models.IntegerField(null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    mobile_number = models.CharField(max_length=12, null = True)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    
    class Meta:
        db_table = "User"
    
    def __str__(self) -> str:
        return self.username