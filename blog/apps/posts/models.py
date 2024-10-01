from django.db import models

# Create your models here.



#Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length = 30, null=False)
    
    def __str__(self):
        return self.nombre
#Post
class Post(models.Model):
    titulo = models.CharField(max_length = 50, null=False)
    subtitulo =  models.CharField(max_length = 100, null=False, blank = True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto =  models.TextField(null=False)
    archivo =  models.FileField(default =True)
    categoria =  models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default = 'Sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to ='media', default =  'static/post_default.jpg')
    publicado = models.DateTimeField()
    
    class Meta:
        ordering = ['-publicado',]
        
    def __str__(self):
        return self.titulo
    
    def delete(self, using =None, kepp_parents =False):
        self.image.delete(self.imagen.name)
        super().delete()


