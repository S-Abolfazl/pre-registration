from django.db import models
from django.contrib.auth import get_user_model

import uuid

User = get_user_model()


class Chat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chat"


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    content = models.TextField(blank=True)

    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE, null=True)

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "message"
