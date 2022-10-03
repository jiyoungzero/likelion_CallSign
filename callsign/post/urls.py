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
    
    
    path('soccer_list/', soccer_list, name="soccer_list"),  
    path('basketball_list/', basketball_list, name="basketball_list"), 
    path('baseball_list/', baseball_list, name="baseball_list"), 
    path('badminton_list/', badminton_list, name="badminton_list"), 
    path('volleyball_list/', volleyball_list, name="volleyball_list"), 
    path('tennis_list/', tennis_list, name="tennis_list"), 
    path('running_list/', running_list, name="running_list"), 
    path('etc_list/', etc_list, name="etc_list"), 
]
