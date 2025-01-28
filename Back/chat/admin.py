from django.contrib import admin
from .models import Message, Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'created', 'updated')
    search_fields = ('sender', 'receiver')
    list_filter = ('created', 'updated')
    readonly_fields = ('id',)
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'sender', 'receiver', 'chat', 'created', 'updated')
    search_fields = ('content', 'sender', 'receiver', 'chat')
    list_filter = ('created', 'updated')
    readonly_fields = ('id',)
