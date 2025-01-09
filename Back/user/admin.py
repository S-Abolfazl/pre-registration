from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'type', 'entry_year', 'first_name', 'last_name', 'mobile_number', 'avatar')
    search_fields = ('username', 'email', 'type', 'entry_year', 'first_name', 'last_name', 'mobile_number')
    list_filter = ('type', 'entry_year')
    readonly_fields = ('id',)