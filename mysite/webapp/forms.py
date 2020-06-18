from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Contrato

class ContratoForm(ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'

class Contrato1Form(ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']