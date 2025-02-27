from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages

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
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "post_list.html", {"posts": posts})

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
