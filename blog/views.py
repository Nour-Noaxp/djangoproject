from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def new(request):
  form = PostForm()
  return render(request, 'blog/new.html', {'form':form})

def create(request):
  form = PostForm()
  if request.method == 'POST':
    print(request.POST)
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Post successfully created")
      return redirect('post_list')
  return render(request, 'blog/new.html', {'form':form})

def home(request):
  categories = ['culture', 'sports', 'food', 'politics', 'religion', 'nature']
  return render(request, 'blog/home.html', {'categories': categories})

def post_list(request):
  posts = Post.objects.all
  return render(request, 'blog/post_list.html', {'posts': posts})

def about(request):
  return render(request, 'blog/about.html')

def contact(request):
  return HttpResponse("This is my contact page displayed with an Http response and not a template rendering")
