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
  Auto('Porsche', 1500000, 48000, 2017, 'gris', "queretaro", "https://m.atcdn.co.uk/vms/media/w1366/23d757c5424f485f92db7f76b028a2cf.jpg" ),
  Auto('Batimovil', 0, 128000, 1963, 'negro', "california", "https://vignette.wikia.nocookie.net/batman/images/8/80/1960%27s_TV_BAtmobile_01.jpg/revision/latest/scale-to-width-down/700?cb=20090609183446"),
  Auto('Lexus', 560000, 12000, 2019, 'rojo', "leon", "https://cmsimages-alt.kbb.com/content/dam/kbb-editorial/make/lexus/lc/2018/lc-500-kbb/01-2018-Lexus-LC-500-Action-KBB.jpg" )
]