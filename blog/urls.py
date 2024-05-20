from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('create/', PostCreateAPIView.as_view()),
    path('list/', PostListAPIView.as_view()),
    path('<int:id>/', PostDetailAPIView.as_view(), name='post_detail'),
    # path('likes/<int:id>/', PostLikesAPIView.as_view()),
    # path('dislikes/<int:id>/', PostDislikesAPIView.as_view()),
    path('<int:post_id>/like/', like_post, name='like_post'),
    path('<int:post_id>/dislike/', dislike_post, name='dislike_post'),
    path('html/', views.index, name='index')
]