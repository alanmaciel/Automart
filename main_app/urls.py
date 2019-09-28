from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^([0-9]+)/$', views.show),
]

# [0-9]+ hace match con cualquier numero
# los parentesis capturan el valor. 
# al capturar el valor este se pasa como parametro
# al detail view, ej. localhost/10
