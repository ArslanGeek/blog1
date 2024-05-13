from django.urls import path
from .views import *

urlpatterns = [
    path('create/', PostCreateAPIView.as_view()),
    path('list/', PostListAPIView.as_view())
]