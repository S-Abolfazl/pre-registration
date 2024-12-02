from django.db import models

from user.models import User
from course.models import AllCourses, Course

class CompletedCourses(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "CompletedCourses"
        unique_together = (('student', 'course'),)
        
    def __str__(self) -> str:
        return f"{self.student.username} - {self.course.courseName}"
    

from django.db import models
import uuid

class EducationalChart(models.Model):
    chart_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    year = models.PositiveIntegerField()
    type = models.CharField(max_length=4, choices=[('odd', 'Odd'), ('even', 'Even')])
    
    term1 = models.JSONField(default=list, blank=True)
    term2 = models.JSONField(default=list, blank=True)
    term3 = models.JSONField(default=list, blank=True)
    term4 = models.JSONField(default=list, blank=True)
    term5 = models.JSONField(default=list, blank=True)
    term6 = models.JSONField(default=list, blank=True)
    term7 = models.JSONField(default=list, blank=True)
    term8 = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = 'EducationalChart'

    def __str__(self):
        return f"Educational Chart {self.year} ({self.type})"
