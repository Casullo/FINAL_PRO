#from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser 
from django.conf import settings


#Create your models here.

class User (AbstractUser):
    icono = models.ImageField (upload_to= 'media/usuarios', null=True, blank=True)
    descripcion = models.TextField (max_length= 250)

    def __str__ (self):
        return self.username
    
class Meta ():
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

#Creación de clase 'categoría'
class Categoria (models.Model):
    nombre = models.CharField (max_length=30, null=False)

    def __str__(self):
        return self.nombre
        
    

class Posts (models.Model):
    titulo = models.CharField (max_length= 50, null= False)
    subtitulo = models.CharField (max_length= 100, null=True, blank=True )
    fecha = models.DateTimeField (auto_now_add=True)
    autor = models.ForeignKey (User, on_delete=models.CASCADE, null=True)
    texto = models.TextField (null=False)
    activo = models.BooleanField (default=True)
    categoria = models.ForeignKey (Categoria, on_delete= models.SET_NULL, null=True, default='Sin categoría' )
    imagen = models.ImageField (null = True, blank=True, upload_to= 'media', default= 'static/post_default.png')
    publicado = models.DateField (default=timezone.now)

    class Meta:
        ordering = ('-publicado' ,)

    def __str__(self):
        return self.titulo
    
#creación clase comentarios

class Comentario (models.Model):
    posts = models.ForeignKey ('posts.Posts', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.texto 