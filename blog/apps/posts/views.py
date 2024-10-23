from django.shortcuts import render

from .models import Posts, User, Comentario, Categoria

from django.shortcuts import redirect

# Create your views here.

#vista basada en clases
from django.views.generic import ListView, DetailView

from .forms import RegistroForm, CrearForm, ModificarForm, ComentarioForm
from django.views.generic import CreateView, DeleteView, UpdateView

class PostListView(ListView):
    model = Posts
    template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        orden = self.request.GET.get('orden')

        #orden por fechas
        if orden == 'reciente':
            queryset = queryset.order_by('-fecha')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha')

        #orden alfabético
        elif orden == 'alfabetico':
            queryset = queryset.order_by('-titulo')

        #ver posts de un determinado autor

        autor = self.request.GET.get("autor")
        if autor:
            queryset = queryset.filter(autor__username= autor)

        #filtro por categoría

        categoria = self.request.GET.get("categoria")
        if categoria:
            queryset = queryset.filter(categoria__nombre=categoria)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.request.GET.get('orden', 'reciente')
        context["categorias"] = Categoria.objects.all()
        return context


class PostDetailView(DetailView):
    model = Posts
    template_name = "posts/post_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Posts.objects.all()

    def get_context_data(self, **kwargs):            # agregar función a detailview para los comentarios
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter (posts_id=self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.posts:post_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        

#crear vista para comentarios

from django.contrib.auth.mixins import LoginRequiredMixin   # mixin que solicita login al usuario

class ComentarioCreateView (LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/agregarComentario.html'
    success_url = 'comentario/comentarios/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs['posts_id']
        return super().form_valid(form)



from django.urls import reverse_lazy
from django.contrib import messages



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



#Sobre nosotros

def about_us(request):
    return render(request, "posts/nosotros.html")

#perfil de usuarios función

def perfil(request, id):
    ctx = {}
    usuarios = User.objects.get(id=id)
    ctx["usuarios"] = usuarios
    print(usuarios)
    return render(request, "perfil.html", ctx)



