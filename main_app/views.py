from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Auto
from .forms import AutoForm


# Create your views here.
def index(request):
  autos = Auto.objects.all()
  form = AutoForm()
  return render(request, 'index.html', {'autos' : autos, 'form' : form})

def show(request, auto_id):
  auto = Auto.objects.get(id=auto_id)
  return render(request, 'show.html', {'auto' : auto})

def post_auto(request):
  form = AutoForm(request.POST)
  if form.is_valid():
    form.save(commit = True)
  return HttpResponseRedirect('/')
