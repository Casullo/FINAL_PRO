from django.contrib import admin
from .models import Categoria, Posts, User

# Register your models here.

#@admin.register (Posts)
class PostsAdmin (admin.ModelAdmin):
    search_fields = ('Titulo',)
    list_filter = ['categoria']
    list_display = ["titulo", "autor", "categoria"]
    date_hierarchy = "publicado"
    

admin.site.register (Categoria) 
admin.site.register (User)
admin.site.register (Posts, PostsAdmin) 



