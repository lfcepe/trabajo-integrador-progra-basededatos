from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Marca, Color_Auto, Tipo_Carro, Iva, Forma_Pago, Cliente, Auto, Kardex, Ventas
# Create your views here.

def index (request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def index_categoria(request):
    template = loader.get_template('index_categorias.html')
    return HttpResponse(template.render(request))

def categoria(request, marca_id, colorauto_id, tipocarro_id, iva_id, formapago_id):
    marca = Marca.objects.get(pk = marca_id)
    colorauto = Color_Auto.objects.get(pk = colorauto_id)
    tipocarro = Tipo_Carro.objects.get(pk = tipocarro_id)
    iva = Iva.objects.get(pk = iva_id)
    formapago = Forma_Pago.objects.get(pk = formapago_id)
    template = loader.get_template('display_categoria.html')
    context = {
        'marca': marca,
        'colorauto': colorauto,
        'tipocarro': tipocarro,
        'iva': iva,
        'formapago': formapago
    }
    return HttpResponse(template.render(context, request))

def display_cliente(request):
    clientes = Cliente.objects.order_by('apellidos')
    template = loader.get_template('display_clientes.html')
    return HttpResponse(template.render({'clientes': clientes}, request))


def display_autos(request):
    autos = Auto.objects.order_by('tipodeauto')
    template = loader.get_template('display_autos.html')
    return HttpResponse(template.render({'autos': autos}, request))


def display_kardex(request):
    kardexs = Kardex.objects.order_by('fechacantidadentrada')
    template = loader.get_template('display_kardex.html')
    return HttpResponse(template.render({'kardexs': kardexs}, request))


def display_ventas(request):
    ventas = Ventas.objects.order_by('fechacompra')
    template = loader.get_template('display_ventas.html')
    return HttpResponse(template.render({'ventas': ventas}, request))
