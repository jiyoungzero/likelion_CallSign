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
    exercises = Exercise.objects.all()
    return render(request, 'post/post_new.html', {'exercise':exercises})

def post_create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    # new_post.writer
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('post:post_detail', new_post.id)

def post_edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'post/post_edit.html', {'post': edit_post})

def post_update(request, id):
    update_post = Post()
    update_post.title = request.POST['title']
    # new_post.writer
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('post:post_detail', update_post.id)

def post_delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect("post:postlist")
    
    
