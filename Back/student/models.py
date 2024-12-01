from django.db import models

from user.models import User
from course.models import AllCourses, Course

import uuid
from PIL import Image
from io import BytesIO

class CompletedCourses(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "CompletedCourses"
        unique_together = (('student', 'course'),)
        
    def __str__(self) -> str:
        return f"{self.student.username} - {self.course.courseName}"
    

class EducationalChart(models.Model):
    Type_Choises = {
        "odd":"odd",
        "even":"even"
    }
    
    chart_id = models.UUIDField(default=uuid.uuid4,primary_key=True, unique=True) 
    year = models.IntegerField()
    type = models.CharField(max_length=20, choices=Type_Choises)
    image = models.BinaryField()
    
    class Meta:
        db_table = "EducationalChart"
    
    def __str__(self) -> str:
        return f"{self.year} - {self.type}"
    
    def save_image(self, image_file):
        if image_file:
            img = Image.open(image_file)
            with BytesIO() as buffer:
                img.save(buffer, format='PNG')
                self.image = buffer.getvalue()
                
    def get_image(self):
        if self.image:
            return BytesIO(self.image)
        return None