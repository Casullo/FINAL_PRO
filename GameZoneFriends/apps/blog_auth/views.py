from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import SingUpForm
from django.contrib.auth import views as auth_views
from django.views.generic import (
    CreateView, 
    ListView, 
    DetailView,
    UpdateView,
    DeleteView,
    )
from .models import Eventos
from .forms import EventoForm
# Create your views here.

class SingUpView(FormView):
    template_name = "registration/register.html"
    form_class = SingUpForm
    success_url = reverse_lazy("apps.blog_auth.views:login")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Login(auth_views.LoginView):
    template_name = "registration/login.html"

class CrearEventoView(CreateView):
    model = Eventos
    form_class = EventoForm
    template_name = "eventos/form_evento.html"
    success_url = reverse_lazy("lista_eventos")

class DetalleEventoView(DetailView):
    model = Eventos
    context_object_name = 'evento'
    template_name = "eventos/detalle_evento.html"

class ListarEventosView(ListView):
    model = Eventos
    context_object_name = 'eventos'
    template_name = "eventos/lista_eventos.html"
    context_object_name = 'eventos'
    paginate_by = 5
    
    def get_queryset(self):
        query = self.request.GET.get('titulo')
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(titulo__icontains=query)
            
        return queryset.order_by('titulo')

class ActualizarEventoView(UpdateView):
    model = Eventos
    form_class = EventoForm
    template_name = "eventos/form_evento.html"
    success_url = reverse_lazy("lista_eventos")

class EliminarEventoView(DeleteView):
    model = Eventos
    form_class = EventoForm
    template_name = "eventos/confirmacion_eliminacion.html"
    success_url = reverse_lazy("lista_eventos")
