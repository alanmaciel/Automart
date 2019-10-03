from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Auto
from .forms import AutoForm
from .models import User

# Create your views here.
def index(request):
  autos = Auto.objects.all()
  form = AutoForm()
  return render(request, 'index.html', {'autos' : autos, 'form' : form})

def show(request, auto_id):
  auto = Auto.objects.get(id=auto_id)
  return render(request, 'show.html', {'auto' : auto})

def post_auto(request):
  form = AutoForm(request.POST, request.FILES)
  if form.is_valid():
    auto = form.save(commit = False)
    auto.user = request.user
    auto.save()

  return HttpResponseRedirect('/')

def profile(request, username):
  user = User.objects.get(username = username)
  autos = Auto.objects.filter(user = user)
  return render(request, 'profile.html', {'username' : username, 'autos': autos})


