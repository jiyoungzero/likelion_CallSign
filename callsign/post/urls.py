from django.urls import path
from .views import *
from . import views

app_name = 'post'
urlpatterns = [
    path('postlist/', postlist, name = "postlist"),
    path('<int:id>/', post_detail, name="post_detail"),
    path('post_new/', post_new, name = "post_new"),
    path('post_create/', post_create, name="post_create"),
]
