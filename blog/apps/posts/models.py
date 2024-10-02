#from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser 


# Create your models here.

#creación de clase ´categoría'
class User (AbstractUser):
    icono = models.ImageField (upload_to= 'media/usuarios', null=True, blank=True)
    descripcion = models.TextField (max_length= 250)

    def __str__ (self):
        return self.username
    
    class Meta ():
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


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
    
    def delete(self, using: None , keep_parents= False):
        self.image.delete (self.imagen.name)
        super().delete()



class Comentarios (models.Model):
    fecha = models.DateTimeField (auto_now_add=True)  #generea fecha y horario automaticamente
    contenido = models.TextField (max_length=250, verbose_name= 'contenido')
    autor= models.ForeignKey (User, on_delete=models.CASCADE, null= True)
    post = models.ForeignKey (Posts, on_delete=models.CASCADE, null= True)



