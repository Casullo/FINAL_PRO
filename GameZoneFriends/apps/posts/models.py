from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField()


class Posts(models.Model):
    titulo= models.CharField(max_length=250, null = False, blank= False, verbose_name="Titulo")
    contenido= models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)