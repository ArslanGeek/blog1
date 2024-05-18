from django.urls import path
from .views import *

urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('logout/', UserLogoutAPIView.as_view()),
    path('profiles/<int:id>/', UserDetailAPIView.as_view()),
    path('sendmessage/', SendMessageAPIView.as_view()),
    path('profiles/', UserListAPIView.as_view()),
]