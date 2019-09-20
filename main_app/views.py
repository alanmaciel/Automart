from django.shortcuts import render

# Create your views here.
def index(request):
  name = "Ford focus"
  model = "2015"
  value = 50000.00
  context = { 'auto_name': name,
              'auto_model': model,
              'auto_value': value }

  return render(request, 'index.html', context)