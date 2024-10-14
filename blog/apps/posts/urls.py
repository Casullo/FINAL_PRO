from django.urls import path
from .views import PostListView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'apps.posts'


urlpatterns = [
    path ('posts/', PostListView.as_view(), name= 'posts'),
    path("registro/", views.Registro.as_view(), name="registro"),
    path('posts/<int:id>', views.PostDetailView.as_view(), name='post_individual'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("nuevo_post/", views.CrearPost.as_view(), name='nuevo_post'),

    path ("eliminar/<int:pk>", views.EliminarPost.as_view(), name = 'eliminar_post'),

    path ("modificar/<int:pk>", views.ModificarPost.as_view(), name = 'modificar_post'),
    
    path("comentar/", views.comentar_post, name="comentar"),

    path("perfil/<int:id>", views.perfil, name="perfil"),
    
    
  
]

