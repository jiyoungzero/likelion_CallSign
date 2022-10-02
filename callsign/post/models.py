from django.db import models

# Create your models here.

# 성별 
# 운동 
# 모집인원
# 운동할날짜

# class Post(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=80)
#     writer = models.CharField(max_length=80)
    
#     body = models.TextField()
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True, verbose_name="등록(수정)일")
    # major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=True, null=True)
   
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]




