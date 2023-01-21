from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import views, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework import authentication, permissions
from .permissions import IsStaffandAuthorPermission
from rest_framework import permissions

from .models import Comment, Post
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)
    def perform_update(self, serializer):
        serializer.save(author=self.request.user.author)
    def perform_destroy(self, serializer):
        serializer.save(author=self.request.user.author)