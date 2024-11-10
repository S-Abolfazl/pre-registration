from django.db import models
import uuid
# Create your models here.
class Course(models.Model):
   
    type = {
      ('specialy_course', 'specialy course'),
      ('elective_course', 'elective course'),
      ('public_course', 'public course'),
      ('basic_course', 'basic course'),
    }

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    course_id = models.CharField(max_length=255)
    courseName = models.CharField(max_length=255)
    teacherName = models.CharField(max_length=255)
    isExperimental = models.BooleanField()
    dateTime = models.DateTimeField(auto_now_add=True)
    exam_dateTime = models.DateTimeField()
    capacity = models.IntegerField()
    type = models.CharField(max_length=30, choices=type)
    
    class Meta:
            db_table = "Course"

    def __str__(self) :
        return self.course_id