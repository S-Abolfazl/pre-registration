from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from course.models import Course
from .models import Notification

@receiver(post_delete, sender=Course)
def create_notification_on_course(sender, instance, **kwargs):
    title = "حذف درس"
    content = [
        "درس",
        f"{instance.course.courseName}",
        "ارائه شده توسط استاد",
        f"{instance.teacherName}",
    ]
    
    if instance.class_time1:
        content.append("در روز")
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
    
@receiver(pre_save, sender=Course)
def create_notification_on_course_update(sender, instance, **kwargs):
    exists = Course.objects.filter(c_id=instance.c_id).exists()
    if exists:
        old_instance = Course.objects.get(c_id=instance.c_id)
        
        if old_instance.teacherName != instance.teacherName:
            title = "تغییر استاد درس"
            content = [
                "استاد درس",
                f"{instance.course.courseName}",
                "از استاد",
                f"{old_instance.teacherName}",
                "به استاد",
                f"{instance.teacherName}",
                "تغییر یافت."
            ]
            
            if instance.class_time1:
                content.append("روز درس:")
                content.append(f"{instance.class_time1}")
                if instance.class_time2 != instance.class_time1:
                    content.append("و")
                    content.append(f"{instance.class_time2}")
                    
                if instance.class_start_time and instance.class_end_time:
                    content.append("ساعت درس:")
                    content.append(f" {str(instance.class_start_time)[:-3]} - {str(instance.class_end_time)[:-3]}")
            
            content = " ".join(content)
            Notification.objects.create(title=title, content=content)
        
        if old_instance.class_time1 != instance.class_time1 and old_instance.class_time2 != instance.class_time2:
            title = "تغییر روز کلاس"
            content = [
                "روز کلاس درس",
                f"{instance.course.courseName}",
                "ارائه شده توسط استاد",
                f"{instance.teacherName}",
                "از",
                f"{old_instance.class_time1}-{old_instance.class_time2}",
                "به",
                f"{instance.class_time1}-{instance.class_time2}",
                "تغییر یافت."
            ]
             
            if instance.class_start_time and instance.class_end_time:
                content.append("ساعت درس:")
                content.append(f" {str(instance.class_start_time)[:-3]} - {str(instance.class_end_time)[:-3]}")
            
            content = " ".join(content)
            Notification.objects.create(title=title, content=content)
        
        if old_instance.class_start_time != instance.class_start_time and old_instance.class_end_time != instance.class_end_time:
            title = "تغییر ساعت کلاس"
            content = [
                "ساعت کلاس درس",
                f"{instance.course.courseName}",
                "ارائه شده توسط استاد",
                f"{instance.teacherName}",
                "از",
                f"{str(old_instance.class_start_time)[:-3]} - {str(old_instance.class_end_time)[:-3]}",
                "به",
                f"{str(instance.class_start_time)[:-3]} - {str(instance.class_end_time)[:-3]}",
                "تغییر یافت."
            ]
            
            if instance.class_time1:
                content.append("روز درس:")
                content.append(f"{instance.class_time1}")
                if instance.class_time2 != instance.class_time1:
                    content.append("و")
                    content.append(f"{instance.class_time2}")
            
            content = " ".join(content)
            Notification.objects.create(title=title, content=content)
    else:
        title = "افزودن درس"
        content = [
            "درس",
            f"{instance.course.courseName}",
            "ارائه شده توسط استاد",
            f"{instance.teacherName}",
        ]
        
        if instance.class_time1:
            content.append("در روز")
            content.append(f"{instance.class_time1}")
            if instance.class_time2 != instance.class_time1:
                content.append("و")
                content.append(f"{instance.class_time2}")
                
            if instance.class_start_time and instance.class_end_time:
                content.append("و در ساعت")
                content.append(f" {str(instance.class_start_time)[:-3]} - {str(instance.class_end_time)[:-3]}")
        
        content.append("افزوده شد")
        
        content = " ".join(content)
        Notification.objects.create(title=title, content=content)
            
            
            