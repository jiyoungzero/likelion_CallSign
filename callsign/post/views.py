from time import time
from post.models import *
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.
def postlist(request):
    posts = Post.objects.all().order_by('end_date')
    
    return render(request, 'post/postlist.html', {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'post/post_detail.html', {'post':post})


def post_new(request):
    exercise = Exercise.objects.all()
    sex = Sex.objects.all()
    return render(request, 'post/post_new.html', {'exercise': exercise, "sex":sex})

def post_create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.url = request.POST['url']
    new_post.exercise = get_object_or_404(Exercise, id=request.POST['exercise'])
    new_post.sex = get_object_or_404(Sex, id=request.POST['sex'])
    # new_post.writer
    new_post.pub_date = timezone.now()
    
    # 모집 시작, 마감일 추가
    new_post.end_date = request.POST['end_date']
    
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('post:post_detail', new_post.id)


def post_edit(request, id):
    edit_post = Post.objects.get(id = id)
    sex = Sex.objects.all()
    exercise = Exercise.objects.all()
    return render(request, 'post/post_edit.html', {'post': edit_post,  'sex':sex, 'exercise': exercise})


def post_update(request, id):
    update_post = Post.objects.get(id=id)
    
    update_post.title = request.POST['title']
    update_post.url = request.POST['url']
    
    
    # try :
    #     update_post.sex = get_object_or_404(Sex, id = request.POST['sex'])
    # except: 
    #     update_post.sex = None
        
    # try :
    #     update_post.exercise = get_object_or_404(Exercise, id = request.POST['exercise'])
    # except: 
    #     update_post.exercise= None
    update_post.sex = get_object_or_404(Sex, id=request.POST['sex'])
    update_post.exercise = get_object_or_404(Exercise, id=request.POST['exercise'])
    # new_post.writer
    update_post.pub_date = timezone.now()
    update_post.end_date = request.POST['end_date']
    
    update_post.body = request.POST['body']
    update_post.save()
    
    return redirect('post:post_detail', update_post.id)

def post_delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect("post:postlist")
    
    
def soccer_list(request):
    soccer_list = []
    s = Exercise.objects.filter(name="축구")
    soccer_post = Post.objects.filter(exercise__in=s)
    
    for post in soccer_post:
        soccer_list.append(post)

    return render(request, 'post/soccer_list.html', {'soccer_list': soccer_list})

def basketball_list(request):
    basketball_list = []
    bsk = Exercise.objects.filter(name="농구")
    bsk_post = Post.objects.filter(exercise__in=bsk)
    
    for post in bsk_post:
        basketball_list.append(post)

    return render(request, 'post/basketball_list.html', {'basketball_list': basketball_list})

def volleyball_list(request):
    volleyball_list = []
    v = Exercise.objects.filter(name="배구")
    v_post = Post.objects.filter(exercise__in=v)
    
    for post in v_post:
        volleyball_list.append(post)

    return render(request, 'post/volleyball_list.html', {'volleyball_list': volleyball_list})

def baseball_list(request):
    baseball_list = []
    b = Exercise.objects.filter(name="야구")
    b_post = Post.objects.filter(exercise__in=b)
    
    for post in b_post:
        baseball_list.append(post)

    return render(request, 'post/baseball_list.html', {'baseball_list': baseball_list})


def tennis_list(request):
    tennis_list = []
    t = Exercise.objects.filter(name="테니스")
    t_post = Post.objects.filter(exercise__in=t)
    
    for post in t_post:
        tennis_list.append(post)

    return render(request, 'post/tennis_list.html', {'tennis_list': tennis_list})

def badminton_list(request):
    badminton_list = []
    b = Exercise.objects.filter(name="배드민턴")
    b_post = Post.objects.filter(exercise__in=b)
    
    for post in b_post:
        badminton_list.append(post)

    return render(request, 'post/badminton_list.html', {'badminton_list': badminton_list})

def running_list(request):
    running_list = []
    r = Exercise.objects.filter(name="산책/러닝")
    r_post = Post.objects.filter(exercise__in=r)
    
    for post in r_post:
        running_list.append(post)

    return render(request, 'post/running_list.html', {'running_list': running_list})

def etc_list(request):
    etc_list = []
    e = Exercise.objects.filter(name="기타")
    e_post = Post.objects.filter(exercise__in=e)
    
    for post in e_post:
        etc_list.append(post)

    return render(request, 'post/etc_list.html', {'etc_list': etc_list})


    
