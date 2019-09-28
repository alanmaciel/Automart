from django.shortcuts import render
from .models import Auto

# Create your views here.
def index(request):
  autos = Auto.objects.all()
  return render(request, 'index.html', {'autos' : autos})

def show(request, auto_id):
  auto = Auto.objects.get(id=auto_id)
  return render(request, 'show.html', {'auto' : auto})