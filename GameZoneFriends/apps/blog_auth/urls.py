from django.urls import path
from views import SingUpView
from django.contrib.auth import views as auth_views
from .views import ListarEventosView, CrearEventoView, DetalleEventoView, ActualizarEventoView, EliminarEventoView

app_name = "apps.blog_auth"

urlpatterns = [
    path("register/", SingUpView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("", ListarEventosView.as_view(), name="lista_eventos"),
    path("<int:pk>/", DetalleEventoView.as_view(), name="detalle_evento"),
    path("editar/<int:pk>/", ActualizarEventoView.as_view(), name="actualizar_evento"),
    path("eliminar/<int:pk>/", EliminarEventoView.as_view(), name="eliminar_evento"),
    path("crear/", CrearEventoView.as_view(), name="crear_evento"),
    ]
