from django.urls import path
from . import views

app_name = 'catalogo_de_autos'

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index_categoria, name="index_categorias"),
    path("", views.display_marca, name="display_marca"),
    path("", views.display_colorauto, name="display_colorauto"),
    path("", views.display_tipocarro, name="display_tipocarro"),
    path("", views.display_iva, name="display_iva"),
    path("", views.display_formapago, name="display_formapago"),
    path("", views.display_cliente, name="display_clientes"),
    path("", views.index_autos, name="index_autos"),
    path("display_autos/< int:id >/", views.display_autos, name="display_autos"),
    path("", views.display_kardex, name="display_kardex"),
    path("", views.display_ventas, name="display_ventas"),
    path('venta/<int:venta_id>/', detalle_venta, name='detalle_venta'),
]
