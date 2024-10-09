from django.shortcuts import render

from .models import Posts

# Create your views here.

#vista basada en clases
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Posts
    template_name = "posts/posts.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Posts
    template_name = "posts/post_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Posts.objects.all()


from .forms import RegistroForm
from django.views.generic import CreateView

from django.urls import reverse_lazy


class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("index")
    template_name = "registro.html"

