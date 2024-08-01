from django.urls import path
from . import views

app_name = 'catalogo_de_autos'

urlpatterns = [
    path("", views.index, name="index"),
    path("index_categorias/", views.index_categoria, name="index_categorias"),
    path("", views.display_marca, name="display_marca"),
    path("", views.display_colorauto, name="display_colorauto"),
    path("", views.display_tipocarro, name="display_tipocarro"),
    path("", views.display_iva, name="display_iva"),
    path("", views.display_formapago, name="display_formapago"),
    path("display_clientes/", views.display_cliente, name="display_clientes"),
    path("index_autos/", views.index_autos, name="index_autos"),
    path("auto/<int:auto_id>/", views.display_autos, name="display_autos"),
    path("index_kardex/", views.index_kardex, name="index_kardex"),
    path("display_ventas/", views.display_ventas, name="display_ventas"),
]
