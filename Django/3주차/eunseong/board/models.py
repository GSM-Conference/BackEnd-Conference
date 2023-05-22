from django.db import models

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=20)
    content = models.TextField()
