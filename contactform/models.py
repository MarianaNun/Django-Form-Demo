from django.db import models

import datetime

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    comment = models.TextField()
    created_date = models.DateTimeField()

