from django.contrib import admin

# Register your models here.

from .models import Categoria, Post

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "contenido", "fecha_publicacion", "autor", "categoria")

admin.site.register(Categoria)