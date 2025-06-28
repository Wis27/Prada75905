from django.urls import path

from . import views
from .views import ClienteDetailView

app_name = "cliente"

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pais/list/", views.pais_list, name="pais_list"),
    path("cliente/list/", views.cliente_list, name="cliente_list"),
    path("cliente/detail/<int:pk>/", views.ClienteDetailView.as_view(), name="cliente_detail"),
]