from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Posts, Comentario


class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200, help_text="Required")
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    icono = forms.ImageField(label="imagen de perfil", required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "icono",
        ]

class CrearForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ["autor"]


class ModificarForm (forms.ModelForm):
    class Meta:

        model = Posts
        fields = ('texto',)

from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class ModificarComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]
        
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario"},
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Ingrese la contraseña"}
        ),
        required=True,
    )
    class Meta:
        model = User
        fields = ["username", "password"]

