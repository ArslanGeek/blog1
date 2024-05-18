from rest_framework import serializers
from .models import *

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = []


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

