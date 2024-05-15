from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from blog.models import Post

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    age = models.PositiveIntegerField(null=True)
    # email = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True, null=True)
    username = models.CharField(max_length=30, unique=True, null=True)
    image = models.FileField(upload_to='', null=True, blank=True)
    is_vip = models.BooleanField(default=False, null=True)

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'






