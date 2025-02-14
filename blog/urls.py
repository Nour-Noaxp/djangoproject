from django.urls import path
from .import views

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("new/", views.new, name="new"),
    path("show/<int:post_id>", views.show, name="show_post"),
    path("edit/<int:post_id>", views.edit, name="edit_post"),
    path("delete/<int:post_id>", views.delete, name="delete_post"),
]
