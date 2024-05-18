from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from blog.models import Post
from .usermanager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    age = models.PositiveIntegerField(null=True)
    # email = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True, null=True)
    username = models.CharField(max_length=30, unique=True, null=True)
    image = models.FileField(upload_to='', null=True, blank=True)
    is_vip = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'








