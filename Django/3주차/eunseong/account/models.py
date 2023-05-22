from django.db import models
class User(models.Model):
    uid = models.CharField(primary_key=True, max_length=100)
    passwd = models.CharField(null=False, max_length=100)
    email = models.EmailField(null=False)
    nickname = models.CharField(max_length=100, null=False)

# Create your models here.
