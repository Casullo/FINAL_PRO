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


from .forms import RegistroForm, CrearForm
from django.views.generic import CreateView, DeleteView

from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect 


class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("login")
    template_name = "registro.html"

    def form_valid(self, form):
        messages.success (self.request, 'Registro exitoso. Por favor, iniciar sesión.')
        return super().form_valid(form)
    
    

class CrearPost(CreateView):
    form_class = CrearForm
    model = Posts
    template_name = "posts/crear_post.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    

class EliminarPost (DeleteView):
    model = Posts
    success_url = reverse_lazy ('index')


