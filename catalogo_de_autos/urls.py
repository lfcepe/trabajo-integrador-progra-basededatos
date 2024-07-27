from django.urls import path
from . import views

app_name = 'catalogo_de_autos'

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index_categoria, name="index_categorias"),
    path("", views.categoria, name="display_marca"),
    path("", views.categoria, name="display_colorauto"),
    path("", views.categoria, name="display_tipocarro"),
    path("", views.categoria, name="display_iva"),
    path("", views.categoria, name="display_formapago"),
    path("", views.display_cliente, name="display_clientes"),
    path("", views.display_autos, name="display_autos"),
    path("", views.display_kardex, name="display_kardex"),
    path("", views.display_ventas, name="display_ventas"),
]
