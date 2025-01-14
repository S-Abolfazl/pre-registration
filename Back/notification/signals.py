from django.db.models.signals import post_delete
from django.dispatch import receiver
from course.models import Course
from .models import Notification

@receiver(post_delete, sender=Course)
def create_notification_on_course(sender, instance, **kwargs):
    title = "حذف درس"
    content = [
        "درس",
        f"{instance.course.corseName}",
        "ارائه شده توسط استاد",
        f"{instance.teacherName}",
        "در روز",
    ]
    
    if instance.class_time1:
        content.append(f"{instance.class_time1}")
        if instance.class_time2 != instance.class_time1:
            content.append("و")
            content.append(f"{instance.class_time2}")
            
        if instance.class_start_time and instance.class_end_time:
            content.append("و در ساعت")
            content.append(f" {str(instance.class_start_time)[:-3]} - {str(instance.class_end_time)[:-3]}")
    
    content.append("حذف شد")
    
    content = " ".join(content)
    Notification.objects.create(title=title, content=content)