from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from .models import *
from .serializer import *

class MessageListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
