from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Auto
from .forms import AutoForm, LoginForm
from .models import User
from django.contrib.auth import authenticate, login, logout

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


def login_view(request):
  if request.method == 'POST':
    # si fue un POST entonces autenticamos el username y el password
    form = LoginForm(request.POST)
    if form.is_valid():
      u = form.cleaned_data['username']
      p = form.cleaned_data['password']
      user = authenticate(username = u, password = p)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/')
        else:
          print("La cuenta esta deshabilitada")
      else:
        print("El usuario o el passw son incorrectos")
  else:
    # si no es un POST simplemente desplegamos la LoginForm

    form = LoginForm()
    return render(request, 'login.html', {'form':form})


def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')