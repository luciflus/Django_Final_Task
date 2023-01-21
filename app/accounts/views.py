from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
