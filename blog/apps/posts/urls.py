from django.urls import path
from .views import PostListView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'apps.posts'



urlpatterns = [
    path ('posts/', PostListView.as_view(), name= 'posts'),
    path("registro/", views.Registro.as_view(), name="registro"),
    path('posts/<int:id>', views.PostDetailView.as_view(), name='post_individual'),
    path("nuevo_post/", views.CrearPost.as_view(), name='nuevo_post'),
    path ("eliminar/<int:pk>", views.EliminarPost.as_view(), name = 'eliminar_post'),
    path ("modificar/<int:pk>", views.ModificarPost.as_view(), name = 'modificar_post'),
    path("nosotros/", views.about_us, name="nosotros"),
    path ("perfil/<int:id>", views.perfil , name="perfil"),
    path("modificar_comementario/<int:pk>", views.ModificarComentario.as_view(), name="modificar_comentario"),
    path( "borrar/<int:pk>", views.EliminarComentario.as_view(), name="borrar_comentario" ),
]

