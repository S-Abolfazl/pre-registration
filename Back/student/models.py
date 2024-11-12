from django.db import models
from user.models import User

class Student(User):
    entry_year = models.IntegerField()
    
    class Meta:
        db_table = "Student"
        
    def __str__(self) -> str:
        return f"{self.username} ({self.entry_year})"
    
# Create your models here.
