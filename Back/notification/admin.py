from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'title', 'content', 'created_at')
    search_fields = ('title', 'content', 'created_at')
    list_filter = ('title',)
    readonly_fields = ('notification_id', 'created_at')
