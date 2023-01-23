from rest_framework import serializers
from .models import Post, Comment, Mark
from django.db.models import Avg
from .bot import bot

from accounts.models import Author

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']

    avg_mark = serializers.SerializerMethodField()
    def get_avg_mark(self, obj):
        return obj.marks.all().aggregate(Avg('mark_value'))

    def create(self, validated_data):
        user = self.context['request'].user
        chat_id = user.author.telegram_chat_id
        from django.db import IntegrityError
        try:
            message = Post.objects.create(**validated_data)
            message.save(
                bot.send_message(chat_id, 'successfully registered')
            )
        except IntegrityError:
            return message


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

