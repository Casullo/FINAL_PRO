from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


#usuarios con atributos nuevos
class User(AbstractUser):
    icono = models.ImageField(upload_to="media/usuarios", # upload_to: es una funcion/propiedad q sirve para decirle de donde viene la imagen
                               null=True, #funcion define que se aceptan nulos osea que no hace falta agregar imagen de perfil
                                 blank=True) #funcion define que puede quedar vacio
    descripcion = models.TextField(max_length=350)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name ="Usuario"
        verbose_name_plural = "Usuarios"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
   
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table ="Categorias"
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

class Post(models.Model):
    titulo= models.CharField(max_length=250, null = False, blank= False, verbose_name="Titulo")
    contenido= models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen =models.ImageField(upload_to="media/posts", null=True,blank=True)

    class Meta:
        db_table ="Posts"
        verbose_name="Post"
        verbose_name_plural="Posts"

    def __str__(self):
        return self.titulo
    
# class Imagenes(models.Model):
#         imagen =models.ImageField(upload_to="/media/Posts")
#         post = models.ForeignKey(Post, on_delete=models.CASCADE)
class Comentarios(models.Model):
    contenido= models.TextField(max_length=250, verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post =models.ForeignKey(Post, on_delete=models.CASCADE )