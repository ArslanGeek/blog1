from django.urls import path
from .views import *

urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('profile/<int:id>/', UserDetailAPIView.as_view()),
    path('sendmessage/', SendMessageAPIView.as_view())
]