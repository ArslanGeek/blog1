# Generated by Django 4.2 on 2024-05-16 10:02

from django.db import migrations
import users.usermanager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', users.usermanager.CustomUserManager()),
            ],
        ),
    ]
