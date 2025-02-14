from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=200, null=False)
  text = models.TextField(null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.title

class Video(models.Model):
  name = models.CharField(max_length=200, null=False)
  url = models.URLField(max_length=200, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.name
