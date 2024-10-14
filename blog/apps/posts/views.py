from django.shortcuts import render

from .models import Posts, User, Comentarios

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


from .forms import RegistroForm, CrearForm, ModificarForm
from django.views.generic import CreateView, DeleteView, UpdateView

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
    success_url = reverse_lazy ("index")


class ModificarPost (UpdateView):
    model = Posts
    form_class = ModificarForm
    template_name = 'posts/modificar_post.html'
    success_url = reverse_lazy ('index')

#comentarios

from django.contrib.auth.decorators import login_required


@login_required
def comentar_post(request):
    comentario = request.POST.get("comentario", None)
    user = request.user
    post = request.POST.get("id_posts", None)
    get_post = Posts.objects.get(pk=post)
    coment = Comentarios.objects.create(autor=user, contenido=comentario, post=get_post)

    return redirect (reverse_lazy ('post_individual', kwargs = {'id': post}))


def perfil(request, id):
    ctx = {}
    usuarios = User.objects.get(id=id)
    ctx["usuarios"] = usuarios
    print(usuarios)
    return render(request, "perfil.html", ctx)







