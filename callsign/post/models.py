from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime, date


# Create your models here.

# 성별 
# 운동 
# 모집인원
# 운동할날짜

# 운동 종류 
# class Exercise(models.Model):
#     Soccer = "축구"
#     BasketBall = "농구"
#     VolleyBall = "배구"
#     BaseBall = "야구"
#     Tennis = "테니스"
#     Badminton = "배드민턴"
#     Running = "산책/러닝"
    
#     EXERCISE_CHOICES = [
#     (Soccer, '축구'),
#     (BasketBall, '농구'),
#     (VolleyBall, '배구'),
#     (BaseBall, '야구'),
#     (Tennis, '테니스'),
#     (Badminton, '배드민턴'),
#     (Running, '산책/러닝'),
#     ]
    
#     exercise_choices = models.CharField(
#         max_length=10,
#         choices=EXERCISE_CHOICES,
#         default=Soccer,
#     )
class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    
    
    def __str__(self):
        return self.name
    
class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    
    
    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length = 300, default="")
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True, verbose_name="등록(수정)일")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, blank=True, null=True) 
       
    flag_enddate = models.BooleanField(default=False)
    
    # 같이 운동할 날짜
    start_date = models.DateField(auto_now=True,editable=True)
    end_date = models.DateField(auto_now=False,editable=True)


    def duration(self):
        return self.end_date - self.start_date

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]




