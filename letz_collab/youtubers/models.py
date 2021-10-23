from django.db import models
from datetime import datetime

# Create your models here.


class Youtuber(models.Model):
    name = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='youtubers/%Y/%m/%d/')
    description = models.TextField()
    city = models.CharField(max_length=100)
    videoUrl = models.URLField()
    subscriber_count = models.IntegerField()
    camera_model = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
