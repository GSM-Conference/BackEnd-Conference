from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(primary_key=True)
    passwd = models.CharField(null=False)
    email = models.EmailField(null=False)
    nickname = models.CharField(max_length=100, null=False)
