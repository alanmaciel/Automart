from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^([0-9]+)/$', views.show),
    url(r'^post_url/$', views.post_auto, name = 'post_auto'),
]

# [0-9]+ hace match con cualquier numero
# los parentesis capturan el valor. 
# al capturar el valor este se pasa como parametro
# al detail view, ej. localhost/10

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT,}),
    ]

# envia cualquier url que haga match con media/ a una view
# de django llamada static.serve()