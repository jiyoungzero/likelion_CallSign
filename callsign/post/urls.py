from django.urls import path
from .views import *
from . import views

app_name = 'post'
urlpatterns = [
    path('postlist/', postlist, name = "postlist"),
    path('<int:id>/', post_detail, name="post_detail"),
    path('post_new/', post_new, name = "post_new"),
    path('post_create/', post_create, name="post_create"),
    path('post_edit/<int:id>', post_edit, name="post_edit"),
    path('post_update/<int:id>', post_update, name="post_update"), 
    path('post_delete/<int:id>', post_delete, name="post_delete"),   
]
