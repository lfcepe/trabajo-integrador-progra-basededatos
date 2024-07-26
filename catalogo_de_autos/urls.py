from django.urls import path
from . import views

app_name = 'catalogo_de_autos'

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index_categoria, name="index_categorias"),
    path("marca/<int:marca_id/>", views.categoria, name="display_categorias"),
    path("colorauto/<int:colorauto_id/>", views.categoria, name="display_categorias"),
    path("tipocarro/<int:tipocarro_id/>", views.categoria, name="display_categorias"),
    path("iva/<int:iva_id/>", views.categoria, name="display_categorias"),
    path("formapago/<int:formapago_id/>", views.categoria, name="display_categorias"),
    path("", views.display_cliente, name="display_clientes"),
    path("", views.display_autos, name="display_autos"),
    path("", views.display_kardex, name="display_kardex"),
    path("", views.display_ventas, name="display_ventas"),
]
