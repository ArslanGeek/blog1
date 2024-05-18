from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework import generics, status
from .serializer import *
from .models import *


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    lookup_field = 'id'

    # def get(self, request, *args, **kwargs):
    #     post_id = kwargs.get('id')
    #     post = get_object_or_404(Post, id=post_id)
    #
    #     if request.accepted_renderer.format == 'html':
    #         likes_count = post.get_likes_count()
    #         dislikes_count = post.get_dislikes_count()
    #         return render(request, 'post_detail.html', {
    #             'post': post,
    #             'likes_count': likes_count,
    #             'dislikes_count': dislikes_count,
    #         })
    #     else:
    #         serializer = self.get_serializer(post)
    #         return Response(serializer.data)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    like = Like.objects.filter(user=user, post=post)
    if like.exists():
        like.delete()
    else:
        Like.objects.create(user=user, post=post)
        Dislike.objects.filter(user=user, post=post).delete()

    data = {
        'likes_count': post.get_likes_count(),
        'dislikes_count': post.get_dislikes_count()
    }
    return JsonResponse(data)

@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    dislike = Dislike.objects.filter(user=user, post=post)
    if dislike.exists():
        dislike.delete()
    else:
        Dislike.objects.create(user=user, post=post)
        Like.objects.filter(user=user, post=post).delete()

    data = {
        'likes_count': post.get_likes_count(),
        'dislikes_count': post.get_dislikes_count()
    }
    return JsonResponse(data)
# class PostLikesAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostLikesSerializer
#     lookup_field = 'id'
#
#     def put(self, request, *args, **kwargs):
#         post_instance = self.get_object()
#         user = request.user
#         likes = request.data.get('likes', [])
#
#         if not likes:
#             return Response({"message": "Likes list is empty."},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         if post_instance.likes.filter(id=user.id).exists():
#             return Response({"message": "You have already liked this post."},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         post_instance.likes.add(user)
#         post_instance.save()
#
#         likes_count = post_instance.likes.count()
#
#         return Response({"likes_count": likes_count},
#                         status=status.HTTP_200_OK)

# class PostDislikesAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDislikesSerializer
#     lookup_field = 'id'
#
#     def put(self, request, *args, **kwargs):
#         post_instance = self.get_object()
#         user = request.user
#         dislikes = request.data.get('dislikes', [])
#
#         if not dislikes:
#             return Response({"message": "Dislikes list is empty."},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         if post_instance.dislikes.filter(id=user.id).exists():
#             return Response({"message": "You have already disliked this post."},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         post_instance.dislikes.add(user)
#         post_instance.save()
#
#         dislikes_count = post_instance.dislikes.count()
#
#         return Response({"likes_count": dislikes_count},
#                         status=status.HTTP_200_OK)





