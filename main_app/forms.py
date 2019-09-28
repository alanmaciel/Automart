from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['nombre', 'valor', 'km', 'modelo', 'color', 'localizacion', 'image'] 