from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    author = models.TextField(null=False)
    title = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
# Create your models here.










