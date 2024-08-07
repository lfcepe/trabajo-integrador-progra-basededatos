from django.urls import path
from . import views

app_name = 'catalogo_de_autos'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("", views.index, name="index"),
    path("index_categorias/", views.index_categoria, name="index_categorias"),
    path("index_categorias/display_marca/", views.display_marca, name="display_marca"),
    path("index_categorias/display_colorauto/", views.display_colorauto, name="display_colorauto"),
    path("index_categorias/display_tipocarro/", views.display_tipocarro, name="display_tipocarro"),
    path("index_categorias/display_iva/", views.display_iva, name="display_iva"),
    path("index_categorias/display_formapago/", views.display_formapago, name="display_formapago"),
    path("index_clientes/", views.index_cliente, name="index_clientes"),
    path("index_autos/", views.index_autos, name="index_autos"),
    path("index_autos/auto/<int:auto_id>/", views.display_autos, name="display_autos"),
    path("index_kardex/", views.index_kardex, name="index_kardex"),
    path("index_ventas/", views.index_ventas, name="index_ventas"),
    #form
    path("add_marca/", views.add_marca, name = "add_marca"),
    path("add_colorauto/", views.add_colorauto, name="add_colorauto"),
    path("add_tipocarro/", views.add_tipocarro, name="add_tipocarro"),
    path("add_iva/", views.add_iva, name="add_iva"),
    path("add_formapago/", views.add_formapago, name="add_formapago"),
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("add_auto/", views.add_auto, name="add_auto"),
    path("add_kardex/", views.add_kardex, name="add_kardex"),
    path("add_venta/", views.add_venta, name="add_venta"),
    #edit
    path("index_categorias/display_marca/edit_marca/<int:id>/", views.edit_marca, name="edit_marca"),
    path("index_categorias/display_colorauto/edit_colorauto/<int:id>/", views.edit_colorauto, name="edit_colorauto"),
    path("index_categorias/display_tipocarro/edit_tipocarro/<int:id>/", views.edit_tipocarro, name="edit_tipocarro"),
    path("index_categorias/display_iva/edit_iva/<int:id>/", views.edit_iva, name="edit_iva"),
    path("index_categorias/display_formapago/edit_formapago/<int:id>/", views.edit_formapago, name="edit_formapago"),
    path("index_clientes/edit_cliente/<int:id>/", views.edit_cliente, name="edit_cliente"),
    path("index_autos/edit_auto/<int:id>/", views.edit_auto, name="edit_auto"),
    path("index_kardex/edit_kardex/<int:id>/", views.edit_kardex, name="edit_kardex"),
    path("index_ventas/edit_venta/<int:id>/", views.edit_venta, name="edit_venta"),
    #delete
    path("index_categorias/display_marca/delete_marca/<int:id>/", views.delete_marca, name="delete_marca"),
    path("index_categorias/display_colorauto/delete_colorauto/<int:id>/", views.delete_colorauto, name="delete_colorauto"),
    path("index_categorias/display_tipocarro/delete_tipocarro/<int:id>/", views.delete_tipocarro, name="delete_tipocarro"),
    path("index_categorias/display_iva/delete_iva/<int:id>/", views.delete_iva, name="delete_iva"),
    path("index_categorias/display_formapago/delete_formapago/<int:id>/", views.delete_formapago, name="delete_formapago"),
    path("index_clientes/delete_cliente/<int:id>/", views.delete_clientes, name="delete_cliente"),
    path("index_autos/delete_auto/<int:id>/", views.delete_autos, name="delete_auto"),
    path("index_kardex/delete_kardex/<int:id>/", views.delete_kardex, name="delete_kardex"),
    path("index_ventas/delete_venta/<int:id>/", views.delete_ventas, name="delete_venta"),
]
