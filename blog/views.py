from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializer import *
from .models import *


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer