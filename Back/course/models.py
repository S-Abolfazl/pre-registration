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

    course_id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True)
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
    
class Prereq(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="prereqs_for")
    prereq_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="is_prereq_of") 
    
    class Meta:
      db_table = "Prereq"
      unique_together = (('course', 'prereq_course'),)

    def __str__(self) :
      return f"{self.course_id} - {self.prereq_id}"



class Rule(models.Model):
    type = {
      ('entry_rule', 'entry_rule'),
    }
    rule_id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True)
    type = models.CharField(max_length=30, choices=type)
    values = models.CharField(max_length=255)
    
    class Meta:
        db_table = "Rule"

    def __str__(self) :
        return self.rule_id
      
class CourseRule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)

    class Meta:
        db_table = "CourseRule"
        unique_together = (('course', 'rule'),)

    def __str__(self) :
        return f"{self.course_id} - {self.rule_id}"