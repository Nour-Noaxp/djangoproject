from django.shortcuts import render, redirect
from .models import Post
from .models import Video
from .forms import PostForm
from .forms import VideoForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User

def new(request):
  form = PostForm()
  users = User.objects.all()
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Post successfully created")
      return redirect("post_list")
  return render(request, "new.html", {"form": form, "users": users})

def home(request):
  categories = ["culture", "sports", "food", "politics", "religion", "nature"]
  return render(request, "home.html", {"categories": categories})

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
  videos = Video.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
  return render(request, "post_list.html", {"posts": posts, "videos": videos})

def feed(request):
  posts = list(Post.objects.filter(published_date__lte=timezone.now()))
  videos = list(Video.objects.filter(published_date__lte=timezone.now()))
  content = sorted(posts + videos, key=lambda x: x.published_date, reverse=True)
  for element in content:
    element.is_video = hasattr(element, "url")
  return render(request, "feed.html", {"content": content})

def get_date(element):
  return element.published_date

def show(request, post_id):
  post = Post.objects.get(pk=post_id)
  return render(request, "show.html", {"post": post})

def delete(request, post_id):
  post = Post.objects.get(pk=post_id)
  post.delete()
  messages.success(request, "Post successfully deleted!")
  return redirect("post_list")

def edit(request, post_id):
  users = User.objects.all()
  post = Post.objects.get(pk=post_id)
  form = PostForm(request.POST or None, instance=post)
  if form.is_valid():
    form.save()
    messages.success(request, "Post successfully updated!")
    return redirect("post_list")
  return render(request, "edit.html", {"post": post, "form": form, "users": users})

def about(request):
  return render(request, "about.html")

def new_video(request):
  form = VideoForm()
  if request.method == "POST":
    form = VideoForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Video successfully created")
      return redirect("post_list")
  return render(request, "new_video.html", {"form": form})

def show_video(request, video_id):
  video = Video.objects.get(pk=video_id)
  return render(request, "show_video.html", {"video": video})

def delete_video(request, video_id):
  video = Video.objects.get(pk=video_id)
  video.delete()
  messages.success(request, "Video successfully deleted!")
  return redirect("post_list")

def edit_video(request, video_id):
  video = Video.objects.get(pk=video_id)
  form = VideoForm(request.POST or None, instance=video)
  if form.is_valid():
    form.save()
    return redirect("post_list")
  return render(request, "edit_video.html", {"video": video, "form": form})
