from django.forms import ModelForm
from .models import Post
from .models import Video

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ["author", "title", "text", "published_date"]

class VideoForm(ModelForm):
  class Meta:
    model = Video
    fields = ["name", "url", "published_date"]
