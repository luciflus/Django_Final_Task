from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    telegram_chat_id = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username
