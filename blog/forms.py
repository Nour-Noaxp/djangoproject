from django.forms import ModelForm, TextInput
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "text", "published_date"]
