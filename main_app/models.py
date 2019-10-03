from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auto(models.Model):
  user = models.ForeignKey(User, on_delete=models.PROTECT)
  nombre = models.CharField(max_length=100)
  valor = models.DecimalField(max_digits=10, decimal_places=2)
  km = models.CharField(max_length=100)
  modelo = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  localizacion = models.CharField(max_length=100)
  img_url = models.CharField(max_length=100)
  image = models.ImageField(upload_to='auto_images',
                            default='media/default.png')

  def __str__(self):
    return self.nombre