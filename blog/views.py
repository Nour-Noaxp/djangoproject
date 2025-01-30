from django.shortcuts import render, HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostForm

def new(request):
  form = PostForm()
  if request.method == 'POST':
    print(request.POST)
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form':form}
  return render(request, 'blog/new.html', context)

def home(request):
  categories = ['culture', 'sports', 'food', 'politics', 'religion', 'nature']
  return render(request, 'blog/home.html', {'categories': categories})

def post_list(request):
  #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  posts = Post.objects.all
  return render(request, 'blog/post_list.html', {'posts': posts})

def about(request):
  return render(request, 'blog/about.html')

def contact(request):
  return HttpResponse("This is my contact page displayed with an Http response and not a template rendering")

