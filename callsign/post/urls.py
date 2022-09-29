from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
    path('postlist/', postlist, name = "postlist"),
    path('post_new/', post_new, name = "post_new"),
]
