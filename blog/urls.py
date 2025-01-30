from django.urls import path
from . import views

urlpatterns = [
  path('posts/', views.post_list, name='post_list'),
  path('', views.home, name='home'),
  path('home/', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('contact/',views.contact, name='contact'),
  path('new/', views.new, name='new')
]
