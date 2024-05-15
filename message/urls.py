from django.urls import path
from .views import *

urlpatterns = [
    path('list/', MessageListAPIView.as_view())
]