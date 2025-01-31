from django.forms import ModelForm, TextInput
from .models import Post

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    widgets = {
      'text': TextInput(attrs={'class': 'h-32'})
    }
    