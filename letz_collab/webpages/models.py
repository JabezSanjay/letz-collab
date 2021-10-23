from os import openpty
from django.db import models
from django.core.validators import FileExtensionValidator


class TeamMembers(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.FileField(upload_to='media/teamMembers/%Y/%m/%d/', validators=[
        FileExtensionValidator(['svg', 'png', 'jpg'])])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HomepageBanner(models.Model):
    title = models.CharField(max_length=200)
    subTitle = models.TextField()
    buttonName = models.CharField(max_length=200, default="Signup here")
    buttonLink = models.CharField(max_length=200, default='signup')
    illustration = models.FileField(upload_to='media/homepageBanner/%Y/', validators=[
                                    FileExtensionValidator(['svg', 'png', 'jpg'])])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
