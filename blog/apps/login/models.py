from django.db import models

# Create your models here.


class User(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre
    
class User_name(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    fecha_nac = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='img_user/post_default.png')
    