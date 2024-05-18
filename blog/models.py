from django.db import models
# from django.contrib.auth.models import Group
from users.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=1000, null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    files = models.FileField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    # likes = models.ManyToManyField('users.CustomUser', related_name='liked_posts', blank=True)
    # dislikes = models.ManyToManyField('users.CustomUser', related_name='disliked_posts', blank=True)

    def get_likes_count(self):
        return self.like_set.count()

    def get_dislikes_count(self):
        return self.dislike_set.count()

    def __str__(self):
        return self.title


class Rate(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
        unique_together = (('user', 'post'),)

class Like(Rate):
    pass

class Dislike(Rate):
    pass







