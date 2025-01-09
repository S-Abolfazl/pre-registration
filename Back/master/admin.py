from django.contrib import admin
from .models import Master

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'education', 'specialization', 'department', 'mobile_number', 'email', 'avatar', 'rate')
    search_fields = ('name', 'education', 'specialization', 'department', 'mobile_number', 'email', 'rate')
    list_filter = ('education', 'specialization', 'department', 'rate')