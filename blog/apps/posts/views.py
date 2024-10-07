from django.shortcuts import render

from .models import Posts

# Create your views here.
def posts (request):
    posts = Posts.objects.all()
    return render (request, 'posts.html', {'posts': posts} )


from .forms import RegistroForm
from django.views.generic import CreateView

from django.urls import reverse_lazy


class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("index")
    template_name = "registro.html"

