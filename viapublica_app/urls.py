from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reclamo/alta/', views.reclamo_alta, name='reclamo_alta'),
    url(r'^vista_reclamos', views.vista_reclamos, name='vista_reclamos'),
    url(r'^classify', views.classify, name='classify')
]
