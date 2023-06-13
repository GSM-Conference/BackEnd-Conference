from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_Post')
    title = models.CharField(max_length=200)
    contents = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
# Create your models here.










