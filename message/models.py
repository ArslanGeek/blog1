from django.db import models
from users.models import CustomUser
from blog.models import Post
class Message(models.Model):
    text = models.TextField(null=True)
    send_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='posts')
    sender_user_id = models.ForeignKey(CustomUser,
                                       on_delete=models.CASCADE,
                                       null=True,
                                       related_name='sent_message')
    receiver_user_id = models.ForeignKey(CustomUser,
                                         on_delete=models.CASCADE,
                                         null=True,
                                         related_name='received_message')


    def __str__(self):
        return self.text