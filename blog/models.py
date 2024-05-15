from django.db import models
# from django.contrib.auth.models import Group
from users.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=1000, null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    files = models.FileField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    likes = models.PositiveIntegerField(null=True)
    dislikes = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title




