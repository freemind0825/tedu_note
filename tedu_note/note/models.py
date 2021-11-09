from django.db import models
from user.models import User
# Create your models here.

class Note(models.Model):
    title = models.CharField('標題', max_length=100)
    content = models.TextField('內容')
    created_time = models.DateTimeField('創建時間', auto_now_add=True)
    updated_time = models.DateTimeField('更新時間', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)