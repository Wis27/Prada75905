from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Pais, Cliente


def index(request):
    return render(request, "cliente/index.html")


def pais_list(request):
    paises = Pais.objects.all()
    contexto = {"paises": paises}
    return render(request, "cliente/pais_list.html", contexto)


def cliente_list(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes}
    return render(request, "cliente/cliente_list.html", contexto)


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente/cliente_detail.html"
