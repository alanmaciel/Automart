from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html', {'autos':autos})

class Auto:
  def __init__(self, nombre, valor, km, modelo, color, localizacion, img_url):
    self.nombre = nombre
    self.valor = valor
    self.km = km
    self.modelo = modelo
    self.color = color
    self.localizacion = localizacion
    self.img_url = img_url


autos = [
  Auto('Ford Focus', 50000, 88000, 2015, 'blanco', "leon", "https://www.autobild.es/sites/autobild.es/public/styles/768x432/public/marcas/fotos/Principal_Lexus.jpg?itok=LRDPS2KG" ),
  Auto('Porsche', 1500000, 48000, 2017, 'gris', "queretaro", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/2016_Lexus_RC_300h_F_Sport_CVT_2.5_Rear.jpg" ),
  Auto('Batimovil', 0, 128000, 1963, 'negro', "california", "https://en.wikipedia.org/wiki/Lincoln_Futura#/media/File:1960s_Batmobile_(FMC).jpg"),
  Auto('Lexus', 560000, 12000, 2019, 'rojo', "leon", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/2016_Lexus_RC_300h_F_Sport_CVT_2.5_Rear.jpg" )
]