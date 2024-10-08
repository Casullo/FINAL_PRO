from django.urls import path
from .views import PostsListView
from . import views

urlpatterns = [
    path("posts/", PostsListView.as_view(), name="posts"),
]