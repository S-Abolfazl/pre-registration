from django.db import models
from django.core.exceptions import ValidationError
import uuid

class Course(models.Model):
    ClassTimeChoices = {
      "شنبه": "شنبه",
      "یکشنبه": "یکشنبه",
      "دوشنبه": "دوشنبه",
      "سه شنبه": "سه شنبه",
      "چهارشنبه": "چهارشنبه",
      "پنجشنبه": "پنجشنبه",
      "جمعه": "جمعه",
    }
  
    c_id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True)
    course = models.ForeignKey('AllCourses', on_delete=models.CASCADE)
    teacherName = models.CharField(max_length=255)
    isExperimental = models.BooleanField()
    class_time1 = models.CharField(max_length=255, choices=ClassTimeChoices, blank=True)
    class_time2 = models.CharField(max_length=255, choices=ClassTimeChoices, blank=True)
    class_start_time= models.TimeField(blank=True, null=True)
    class_end_time = models.TimeField(blank=True, null=True)
    exam_date = models.DateField(blank=True, null=True)
    exam_start_time = models.TimeField(blank=True, null=True)
    exam_end_time = models.TimeField(blank=True, null=True)
    capacity = models.PositiveIntegerField(default=0)
    registered = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
            db_table = "Course"

    def __str__(self) :
        return f"{self.c_id}"

class AllCourses(models.Model):
    CourseType = {
      ('theory_course', 'theory course'), # theory
      ('practical_course', 'practical course'), #amali
      ('elective_course', 'elective course'), #ekhtiari
      ('basic_course', 'basic course'), #paye
      ('public_course', 'public course'), #omumi
    }
    
    course_id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True)
    courseName = models.CharField(max_length=255, unique=True)
    unit = models.PositiveIntegerField()
    type = models.CharField(max_length=30, choices=CourseType)

    class Meta:
        db_table = "AllCourses"
        
    def __str__(self) :
        return str(self.courseName)
    
class Prereq(models.Model):
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE, related_name="prereqs_for")
    prereq_course = models.ForeignKey(AllCourses, on_delete=models.CASCADE, related_name="is_prereq_of") 
    
    class Meta:
      db_table = "Prereq"
      unique_together = (('course', 'prereq_course'),)
      
    def clean(self):
        if self.course == self.prereq_course:
            raise ValidationError("درس و درس پیشنیاز نمی‌توانند یکسان باشند")

    def __str__(self) :
      return f"{self.course.course_id} - {self.prereq_course.course_id}"

class Coreq(models.Model):
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE, related_name="coreqs_for")
    coreq_course = models.ForeignKey(AllCourses, on_delete=models.CASCADE, related_name="is_coreq_of") 
    
    class Meta:
      db_table = "Coreq"
      unique_together = (('course', 'coreq_course'),)
      
    def clean(self):
        if self.course == self.coreq_course:
            raise ValidationError("درس و درس هم‌نیاز نمی‌توانند یکسان باشند")

    def __str__(self) :
      return f"{self.course.course_id} - {self.coreq_course.course_id}"
      
class CourseRule(models.Model):
    typeChoice = {
      ('entry_rule', 'entry_rule'),
    }
    rule_id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=typeChoice)
    values = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = "CourseRule"

    def __str__(self) :
        return f"{self.course.c_id}"



