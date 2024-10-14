from django.shortcuts import render
from .models import Post
# Create your views here.
# vistas basadas en funciones
def posts(request):
    ctx =  {}
    noticias = Post.objects.all() # select * from Posts
    ctx['noticias'] = noticias
    return render(request,  'posts/posts.html', ctx)

def about_us(request):
    return render(request,  'posts/about_us.html')

def registro(request):
    return render(request,  'usuarios/registro.html')  
