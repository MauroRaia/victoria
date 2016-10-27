from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reclamo/alta/', views.reclamo_alta, name='reclamo_alta')
] 
