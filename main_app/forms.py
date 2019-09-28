from django import forms

class AutoForm(forms.Form):
  nombre = forms.CharField(label='Nombre', max_length=100)
  valor = forms.DecimalField(label='Precio', max_digits=10, decimal_places=2)
  km = forms.CharField(label='Km', max_length=100)
  modelo = forms.CharField(label='Modelo', max_length=100)
  color = forms.CharField(label='Color', max_length=100)
  localizacion = forms.CharField(label='Localizacion', max_length=100)
  img_url = forms.CharField(label='Imagen URL', max_length=100)