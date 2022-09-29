from django.urls import path
from .views import *
from . import views

app_name = 'post'
urlpatterns = [
    path('postlist/', postlist, name = "postlist"),
    path('post_new/', post_new, name = "post_new"),
    # path("category/<str:category_name>/", views.CategoryView, name="category"),
]
