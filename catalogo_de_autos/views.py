from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Catalogos, Clientes, Autos, Kardex, Ventas
# Create your views here.

def index (request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def index_catalogo(request):
    catalogos = Catalogos.objects.order_by('catalogo')
    template = loader.get_template('index_catalogos.html')
    return HttpResponse(template.render({'catalogos': catalogos}, request))

def catalogo(request, catalogo_id):
    catalogo = Catalogos.objects.get(pk = catalogo_id) 
    nombrecatalogo = Catalogos.objects.get(catalogo = catalogo)
    template = loader.get_template('display_catalogos.html')
    context = {
        'catalogo': catalogo,
        'nombrecatalogo': nombrecatalogo
    }
    return HttpResponse(template.render(context, request))

def index_cliente(request):
    clientes = Clientes.objects.order_by('apellidos')
    template = loader.get_template('index_clientes.html')
    return HttpResponse(template.render({'clientes': clientes}, request))

def cliente (request, cliente_id):
    cliente = Clientes.objects.get(pk = cliente_id)
    template = loader.get_template('display_clientes.html')
    context = {
        'cliente': cliente
    }
    return HttpResponse(template.render(context, request))

def index_autos(request):
    autos = Autos.objects.order_by('modelo')
    template = loader.get_template('index_autos.html')
    return HttpResponse(template.render({'autos': autos}, request))

def auto (request, auto_id):
    auto = Autos.objects.get(pk = auto_id)
    template = loader.get_template('display_autos.html')
    context = {
        'auto': auto
    }
    return HttpResponse(template.render(context, request))

def index_kardex(request):
    kardex = Catalogos.objects.order_by('id_auto')
    template = loader.get_template('index_kardex.html')
    return HttpResponse(template.render({'kardex': kardex}, request))

def kardex (request, kardex_id):
    kardex = Kardex.objects.get(pk = kardex_id)
    template = loader.get_template('display_kardex.html')
    context = {
        'kardex': kardex
    }
    return HttpResponse(template.render(context, request))

def index_ventas(request):
    ventas = Catalogos.objects.order_by('valortotalapagar')
    template = loader.get_template('index_ventas.html')
    return HttpResponse(template.render({'ventas': ventas}, request))

def venta (request, venta_id):
    venta = Kardex.objects.get(pk = venta_id)
    template = loader.get_template('display_venta.html')
    context = {
        'venta': venta
    }
    return HttpResponse(template.render(context, request))