from django.contrib import admin

# Register your models here.

from .models import Categoria, Post, User

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    search_fields = ("titulo",)
    list_display = ("id", "titulo", "contenido", "fecha_publicacion", "autor", "categoria")
    list_filter =["categoria", "autor__username"] # <---- hace referencia al campo username de la tabla post_user
admin.site.register(Categoria)
admin.site.register(User)