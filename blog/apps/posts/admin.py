from django.contrib import admin
from .models import Categoria, Posts

# Register your models here.

@admin.register (Posts)
class PostsAdmin (admin.ModelAdmin):
    listdisplay = ('Id', 'título', 'subtítulo', 'fecha', 'texto', 'activo', 
                   'categoría', 'imagen', 'publicado' )
    
    admin.site.register (Categoria)

