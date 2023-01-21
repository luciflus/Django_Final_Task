from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Author(models.Model):
    username = models.CharField(max_length=50)
    telegram_chat_id = models.CharField(max_length=255)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.username