from time import time
from post.models import *
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.
def postlist(request):
    posts = Post.objects.all()
    return render(request, 'post/postlist.html', {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'post/post_detail.html', {'post':post})


def post_new(request):
    return render(request, 'post/post_new.html')

def post_create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    # new_post.writer
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('post:post_detail', new_post.id)
