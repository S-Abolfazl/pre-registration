from django.db import models
import uuid

from user.models import User

class SupportChat(models.Model):
    chat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    support = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    creationDateTime = models.DateTimeField(auto_now_add=True)
    lastUpdate_DateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chat ID: {self.chat_id}, User ID: {self.user.id}, Support ID: {self.support.id}"

    class Meta:
        db_table = 'SupportChat'
        

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    chat = models.ForeignKey(SupportChat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    creationDateTime = models.DateTimeField(auto_now_add=True)
    seenBySupport = models.BooleanField(default=False)
    def __str__(self):
        return f"Message ID: {self.message_id}, Chat ID: {self.chat.chat_id}, Sender ID: {self.sender.id}"

    class Meta:
        db_table = 'Message'