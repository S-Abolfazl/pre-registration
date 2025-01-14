from django.db import models
import uuid

class Notification(models.Model):
    notification_id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        db_table = "Notification"

    def __str__(self) :
        return self.title
