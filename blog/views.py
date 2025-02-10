from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm
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
    return render(request, "blog/new.html", {"form": form, "users": users})


def home(request):
    categories = ["culture", "sports", "food", "politics", "religion", "nature"]
    return render(request, "blog/home.html", {"categories": categories})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "blog/post_list.html", {"posts": posts})

def show(request, pk):
    return render(request, "blog/show.html", {"pk": pk})

def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("post_list")

def edit(request, pk):
    form = PostForm()
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form.PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post successfully updated")
            return redirect("post_list")
    return render (request, "blog/edit.html", {"form": form, "pk": pk})

def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return HttpResponse(
        "This is my contact page displayed with an Http response and not a template rendering"
    )
