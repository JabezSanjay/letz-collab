from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.


class Youtuber(models.Model):

    camera_model_choices = (
        ('Canon', 'Canon'),
        ('Nikon', 'Nikon'),
        ('Sony', 'Sony'),
        ('Panasonic', 'Panasonic'),
        ('Olympus', 'Olympus'),
        ('Fujifilm', 'Fujifilm'),
        ('Pentax', 'Pentax'),
        ('Other', 'Other'),
    )
    category_choices = (
        ('Music', 'Music'),
        ('Sports', 'Sports'),
        ('News', 'News'),
        ('Entertainment', 'Entertainment'),
        ('Education', 'Education'),
        ('Lifestyle', 'Lifestyle'),
        ('Gaming', 'Gaming'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='youtubers/%Y/%m/%d/')
    description = RichTextField()
    price = models.IntegerField(default=0)
    country = models.CharField(max_length=100)
    videoUrl = models.URLField()
    subscriber_count = models.IntegerField()
    camera_model = models.CharField(
        max_length=100, choices=camera_model_choices)
    category = models.CharField(max_length=100, choices=category_choices)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
