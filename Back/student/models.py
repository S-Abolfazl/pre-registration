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