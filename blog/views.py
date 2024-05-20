from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
# from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework import generics, status
from .serializer import *
from .models import *


def index(request):
    return render(request, 'myapp/index.html')

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.validated_data['user_id'] = request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'Not authenticated user'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    # permission_classes = [IsAuthenticated]


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    lookup_field = 'id'


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    print(request.user)

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




