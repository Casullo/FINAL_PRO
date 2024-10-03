from django.contrib import admin

# Register your models here.

from .models import Categoria, Post, User

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "contenido", "fecha_publicacion", "autor", "categoria")

admin.site.register(Categoria)
admin.site.register(User)