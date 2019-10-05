from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['nombre', 'valor', 'km', 'modelo', 'color', 'localizacion', 'image'] 

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Usuario', max_length=64)
    password = forms.CharField(widget = forms.PasswordInput())

