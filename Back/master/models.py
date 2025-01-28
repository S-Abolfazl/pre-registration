from django.db import models
import uuid

class Master(models.Model):

    role = {
        ('assistant_professor', 'استادیار'),
        ('associate_professor', 'دانشیار'),
        ('full_professor', 'استاد تمام'),

    }
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True)
    name = models.CharField(max_length = 255 , null = True, blank = True)
    #last_name = models.CharField(max_length = 255 , null = True, blank = True)
    education = models.CharField(max_length = 255 , null = True, blank = True)
    specialization = models.CharField(max_length = 255 , null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    department =  models.CharField(max_length = 255 , null = True, blank = True)
    mobile_number = models.CharField(max_length = 11 , null = True, blank = True)
    email = models.EmailField(null= True)
    avatar = models.ImageField(upload_to = 'masters/', null = True)
    rate = models.IntegerField(null = True, blank = True)


    class Meta:
        db_table = "Master"
    def __str__(self):
        return f"{self.name}"