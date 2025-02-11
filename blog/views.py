from django.shortcuts import render, HttpResponse, redirect
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
    return render(request, "events/new.html", {"form": form, "users": users})

def home(request):
    categories = ["culture", "sports", "food", "politics", "religion", "nature"]
    return render(request, "events/home.html", {"categories": categories})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "events/post_list.html", {"posts": posts})

def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "events/show.html", {"post": post})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.success(request, "Post successfully deleted!")
    return redirect("post_list")
# return Response({ "message": "Post successfully deleted!"})

def edit(request, post_id):
    users = User.objects.all()
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("post_list")
    return render(request, "events/edit.html", {"post": post, "form": form, "users": users})

def about(request):
    return render(request, "events/about.html")

def contact(request):
    return HttpResponse(
        "This is my contact page displayed with an Http response and not a template rendering"
    )
