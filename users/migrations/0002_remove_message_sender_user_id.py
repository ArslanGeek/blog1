# Generated by Django 4.2 on 2024-05-15 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='sender_user_id',
        ),
    ]
