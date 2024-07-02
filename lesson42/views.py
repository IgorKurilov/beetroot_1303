# views.py
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes, 'dislikes': post.dislikes, 'rating': post.rating})

def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.dislikes += 1
    post.save()
    return JsonResponse({'likes': post.likes, 'dislikes': post.dislikes, 'rating': post.rating})
