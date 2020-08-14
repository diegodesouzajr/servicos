from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciar_servico_tres', views.iniciar_servico_tres, name='iniciar_servico_tres'),
]
