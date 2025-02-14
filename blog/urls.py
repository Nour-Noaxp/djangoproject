from django.urls import path
from .import views

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("feed/", views.feed, name="feed"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("new/", views.new, name="new"),
    path("show/<int:post_id>", views.show, name="show_post"),
    path("edit/<int:post_id>", views.edit, name="edit_post"),
    path("delete/<int:post_id>", views.delete, name="delete_post"),
    path("new_video/", views.new_video, name ="new_video"),
    path("show_video/<int:video_id>", views.show_video, name="show_video"),
    path("edit_video/<int:video_id>", views.edit_video, name="edit_video"),
    path("delete_video/<int:video_id>", views.delete_video, name="delete_video"),
]
