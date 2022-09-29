from django.shortcuts import render
from post.models import *

# Create your views here.
def postlist(request):
    
    # category_posts = models.Post.objects.filter(category=category_name)
    # categories = models.Category.objects.all()
    # return render(
    #     request,
    #     "post/postlist.html",
    #     {
    #         "category_name": category_name,
    #         "category_posts": category_posts,
    #         "categories": categories,
    #     },
    # )
    return render(request, 'post/postlist.html')

def post_new(request):
    return render(request, 'post/post_new.html')
