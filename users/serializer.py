from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser
from message.models import Message
from blog.serializer import PostsSerializer

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'text',
            'send_post',
            'receiver_user_id',
            'sender_user_id',
        ]




class UserProfileSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'age',
            'created_at',
            'image',
            'is_vip',
            'messages'

        ]

    def get_messages(self, obj):
        messages = obj.received_message.all()
        return MessageSerializer(messages, many=True).data



