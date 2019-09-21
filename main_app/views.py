from django.shortcuts import render
from .models import Auto

# Create your views here.
def index(request):
  autos = Auto.objects.all()
  return render(request, 'index.html', {'autos' : autos})
