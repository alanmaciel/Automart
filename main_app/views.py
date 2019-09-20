from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html', {'autos':autos})

class Auto:
  def __init__(self, nombre, valor, km, modelo, color, localizacion):
    self.nombre = nombre
    self.valor = valor
    self.km = km
    self.modelo = modelo
    self.color = color
    self.localizacion = localizacion


autos = [
  Auto('Ford Focus', 50000, 88000, 2015, 'blanco', "leon" ),
  Auto('Porsche', 1500000, 48000, 2017, 'gris', "queretaro" ),
  Auto('Batimovil', 0, 128000, 1963, 'negro', "california" ),
  Auto('Lexus', 560000, 12000, 2019, 'rojo', "leon" )
]