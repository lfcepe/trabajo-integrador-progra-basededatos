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


def display_marca(request):
    marcas = Marca.objects.order_by('marca')
    template = loader.get_template('display_marca.html')
    return HttpResponse(template.render({'marcas': marcas})(request))

def obtener_marca(marca_id):
    marca = Marca.objects.get(pk = marca_id)
    return {'marca': marca}    

def display_colorauto(request):
    colores = ColorAuto.objects.order_by('colorauto')
    template = loader.get_template('display_colorauto.html')
    return HttpResponse(template.render({'colores' : colores})(request))

def obtener_colores(color_id):
    color = ColorAuto.objects.get(pk = color_id)
    return {'color': color}
    
def display_tipocarro(request):
    tipos = TipoCarro.objects.order_by('modelocarro')
    template = loader.get_template('display_tipocarro.html')
    return HttpResponse(template.render({'tipos': tipos})(request))

def obtener_tipocarro(tipo_id):
    tipo = TipoCarro.objects.get(pk= tipo_id)
    return {'tipo': tipo}


def display_iva(request):
    piva = Iva.objects.order_by('valordecalculo')
    template = loader.get_template('display_iva.html')
    return HttpResponse(template.render({'piva': piva})(request))

def obtener_iva(iva_id):
    iva = Iva.objects.get(pk = iva_id)
    return {'iva': iva}
    
def display_formapago(request):
    pagos = FormaPago.objects.order_by('formadepago')
    template = loader.get_template('display_formapago.html')
    return HttpResponse(template.render({'pagos': pagos})(request))

def obtener_formadepago(formadepago_id):
    pago = FormaPago.objects.get(pk = formadepago_id)
    return {'pago': pago}

def display_cliente(request):
    clientes = Cliente.objects.order_by('apellido')
    templade = loader.get_template('display_clientes.html')
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

def obtener_kardex(kardex_id):
    kardex = Kardex.objects.get(pk = kardex_id)
    return {'kardex': kardex}

def display_ventas(request):
    ventas = Venta.objects.order_by('fechacompra')
    template = loader.get_template('display_ventas.html')
    return HttpResponse(template.render({'ventas': ventas}, request))
