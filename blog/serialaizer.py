from rest_framework import serializers
from .models import *


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'