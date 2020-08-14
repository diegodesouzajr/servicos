from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm


from .models import ServicoUm, ServicoDois, ServicoTres, ServicoQuatro
from .forms import ServicoUmForm


def index(request):
    return render(request, "servicos/index.html", {'title': 'Serviço 3:'})


def iniciar_servico_tres(request):
    qs = ServicoTres.objects.all()
    if qs:
        print('not ok')

    qs_um = ServicoUm.objects.all()
    qs_dois = ServicoDois.objects.all()

    quantidade_1 = len(qs_um)
    quantidade_2 = len(qs_dois)

    qtd = quantidade_1
    if qtd > quantidade_2:
        qtd = quantidade_2

    contador = 0
    detail_list = []

    #for i in range(qtd):
    for i in range(500):
        multiplica = list(qs_um.values_list())[i][1] * list(qs_dois.values_list())[i][1]

        if multiplica > 100000:
            SQ = ServicoQuatro(numero_publicado=multiplica)
            SQ.save()

            detail_list.append(multiplica)
            contador += 1

    txt = 'Serviço 4: %s números publicados' % contador
    return render(request, "servicos/index_s4.html", {'title': txt, 'detail_list': detail_list})
