from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Author
from django.core.validators import MaxValueValidator, MinValueValidator


class Post(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} - {self.created_at} - {self.author}'


class Comment(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} - {self.created_at} - {self.author}'


class Mark(models.Model):
    mark_value = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='marks')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mark_value}'
