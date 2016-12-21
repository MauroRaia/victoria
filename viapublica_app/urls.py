from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reclamo/alta/', views.reclamo_alta, name='reclamo_alta'),
    url(r'^vista_reclamos', views.vista_reclamos, name='vista_reclamos'),
    url(r'^classify', views.classify, name='classify'),
    url(r'^clasificar/(?P<pk>[0-9]+)/$', views.clasificar, name='clasificar'),
    url(r'^showMap/(?P<pk>[0-9]+)/$', views.showMap, name='showMap')
]
