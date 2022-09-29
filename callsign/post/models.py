from django.db import models

from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("home")


class Post(models.Model):
    category = models.CharField(max_length=30, default="축구")
    title = models.CharField(max_length=80)
    # writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:20]