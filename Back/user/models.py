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
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    type = models.CharField(max_length=30, choices=USER_TYPE)
    
    class Meta:
        db_table = "User"
    
    def __str__(self) -> str:
        return self.username