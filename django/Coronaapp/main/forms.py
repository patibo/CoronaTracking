from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Kunden
from django import forms



class KundenForm(ModelForm):
    class Meta:
        model = Kunden
        fields = '__all__'

class LoginForm(ModelForm):
    class Meta:
        model = Kunden
        fields = ['benutzername', 'email', 'passwort']