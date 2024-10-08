from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"