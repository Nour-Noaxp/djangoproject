from django.urls import path
from .import views

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("new/", views.new, name="new"),
    path("show/<post_id>", views.show, name="show_post"),
    path("edit/<post_id>", views.edit, name="edit_post"),
    path("delete/<int:pk>", views.delete, name="delete_post"),

    path("new_video/", views.new_video, name ="new_video"),
    path("show_video/<video_id>", views.show_video, name="show_video"),
    path("edit_video/<video_id>", views.edit_video, name="edit_video"),
    path("delete_video/<int:pk>", views.delete_video, name="delete_video"),
]   
