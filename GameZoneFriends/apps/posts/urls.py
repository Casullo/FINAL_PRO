# urls solo de la app posts
from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts),
    path("about/", views.about_us),
    path("registro/", views.registro),

]