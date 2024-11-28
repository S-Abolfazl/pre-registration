from django.db import models
import uuid

from user.models import User
from course.models import Course

class RegistrationForm(models.Model):
    form_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    student_id = models.OneToOneField(User, related_name='registration_form_student', on_delete=models.SET_NULL,
                                      null=True,
                                      unique=True)
    creationDateTime = models.DateTimeField(auto_now_add=True)
    lastUpdate_DateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Form ID: {self.form_id}, Student ID: {self.student_id}"

    class Meta:
        db_table = 'RegistrationForm'


class SelectedCourse(models.Model):
    form = models.ForeignKey(RegistrationForm, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'SelectedCourse'
        unique_together = (('form', 'course'),)

    def __str__(self):
        return f"Form ID: {self.form.form_id}, Course ID: {self.course.course_id}"