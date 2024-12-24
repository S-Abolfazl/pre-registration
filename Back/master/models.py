from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Master(models.Model):

    Master_type = {
        ('assistant_professor', 'استادیار'),
        ('associate_professor', 'دانشیار'),
        ('full_professor', 'استاد تمام'),

    }
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True)
    first_name = models.CharField(max_length = 255 , null = True, blank = True)
    last_name = models.CharField(max_length = 255 , null = True, blank = True)
    education = models.CharField(max_length = 255 , null = True, blank = True)
    specialization = models.CharField(max_length = 255 , null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    department =  models.CharField(max_length = 255 , null = True, blank = True)


    class Meta:
        db_table = "Master"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"