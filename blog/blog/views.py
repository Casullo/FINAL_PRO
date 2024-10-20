from django.shortcuts import render
from django.http import request
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def index (request):
    return render (request, 'index.html')

def custom_logout(request):
    logout(request)  # Cierra la sesión
    return render(request, 'logout.html')



