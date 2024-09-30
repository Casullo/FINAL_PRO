from django.shortcuts import render
from .models import User_name

# Create your views here.

def login(request):
    login = User_name.objects.all()
    return render(request, 'login.html', {'login': login})