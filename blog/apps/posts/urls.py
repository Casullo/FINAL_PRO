from django.urls import path
from .views import posts
from . import views


urlpatterns = [
    path ('posts/', posts, name= 'posts'),
    path("registro/", views.Registro.as_view(), name="registro"),

]