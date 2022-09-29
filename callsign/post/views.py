from django.shortcuts import render

# Create your views here.
def postlist(request):
    return render(request, 'post/postlist.html')

def post_new(request):
    return render(request, 'post/post_new.html')