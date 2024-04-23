from django.db import models

# Create your models here.

class User(models.Model):

    id = models.IntegerField(primary_key=True)#主键
    username = models.CharField(max_length=30)#用户名，字符串类型

    email = models.CharField(max_length=30)#邮件，字符串类型

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120)
    context = models.TextField()
    publish_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)#多个Article对应一个User