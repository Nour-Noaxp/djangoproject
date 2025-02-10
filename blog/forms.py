from django.forms import ModelForm, TextInput
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "text", "published_date"]
        # widgets = {"text": TextInput(attrs={"class": "h-32"})}
