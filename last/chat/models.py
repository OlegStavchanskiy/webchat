from django.contrib.auth.models import User
from django.db import models


class ChatRoom(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'self.title. Id: {self.id}'


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_read = models.BooleanField(default=False)  # Добавлено поле прочтения

    def __str__(self):
        return self.content

