from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Marca, ColorAuto, TipoCarro, Iva, FormaPago, Cliente, Auto, Kardex, Venta
# Create your views here.

def index (request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def index_categoria(request):
    template = loader.get_template('index_categorias.html')
    return HttpResponse(template.render(request))

def display_categoria(request):
    template = loader.get_template('display_categoria.html')
    return HttpResponse(template.render(request))

def display_marca(request):
    
def display_colorauto(request):
    
def display_tipocarro(request):

def display_iva(request):
    
def display_formapago(request):



def display_cliente(request):
    clientes = Cliente.objects.order_by('apellido')
    templade = loader.get_templade('display_clientes.html')
    return HttpResponse(templade.render({'clientes': clientes}), request)

def index_autos(request):
    auto = Auto.objects.order_by('modelo')
    template = loader.get_template('index_autos.html')
    return HttpResponse(template.render({'auto': auto}, request))

def display_autos(request, autos_id):
    autos = Auto.objects.get(pk= autos_id)
    template = loader.get_template('display_autos.html')
    context = {
        'autos': autos
    }
    return HttpResponse(template.render(context, request))


def display_kardex(request):
    kardexs = Kardex.objects.order_by('fechacantidadentrada')
    template = loader.get_template('display_kardex.html')
    return HttpResponse(template.render({'kardexs': kardexs}, request))


def display_ventas(request):
    ventas = Venta.objects.order_by('fechacompra')
    template = loader.get_template('display_ventas.html')
    return HttpResponse(template.render({'ventas': ventas}, request))
