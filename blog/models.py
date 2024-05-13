from django.db import models
from django.contrib.auth.models import Group

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    # user_id = models.ForeignKey(models.CASCADE)
    files = models.FileField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    likes = models.PositiveIntegerField(null=True)
    dislikes = models.PositiveIntegerField(null=True)

class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    # sender_user_id = models.ForeignKey(models.CASCADE)
    # reciepent_user_id = models.ForeignKey(models.CASCADE)


