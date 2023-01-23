from rest_framework import serializers

from .models import Post, Comment, Mark
from django.db.models import Avg
from accounts.models import Author

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']

    avg_mark = serializers.SerializerMethodField()
    def get_avg_mark(self, obj):
        return obj.marks.all().aggregate(Avg('mark_value'))


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        #read_only_fields = ['author']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'
        read_only_fields = ['author', ]

