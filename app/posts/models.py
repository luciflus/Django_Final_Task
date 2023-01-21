from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Author
from django.core.validators import MaxValueValidator, MinValueValidator


class Post(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def get_avg(self):
        # all_marks = Mark.objects.all()
        result = Mark.objects.filter(mark_value=self)
        # result = {}
        # for m in all_marks:
        #     result[m.name] = 0
        #     for i in g_mark:
        #         if s_tweet.type == s_type:
        #             result[s_type.name] += 1
        print(result)

    def __str__(self):
        return f'{self.text} - {self.created_at} - {self.author} - {self.get_avg}'


class Comment(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} - {self.created_at} - {self.author}'


class Mark(models.Model):
    mark_value = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.mark_value}'
