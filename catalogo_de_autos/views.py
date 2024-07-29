from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from .models import Marca, ColorAuto, TipoCarro, Iva, FormaPago, Cliente, Auto, Kardex, Venta

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def index_categoria(request):
    template = loader.get_template('index_categorias.html')
    return HttpResponse(template.render(request))

def display_categoria(request):
    template = loader.get_template('display_categoria.html')
    return HttpResponse(template.render(request))

def display_marca(request):
    template = loader.get_template('display_marca.html')
    return HttpResponse(template.render(request))

def display_colorauto(request):
    template = loader.get_template('display_colorauto.html')
    return HttpResponse(template.render(request))
    
def display_tipocarro(request):
    template = loader.get_template('display_tipocarro.html')
    return HttpResponse(template.render(request))

def display_iva(request):
    template = loader.get_template('display_iva.html')
    return HttpResponse(template.render(request))
    
def display_formapago(request):
    template = loader.get_template('display_formapago.html')
    return HttpResponse(template.render(request))

def display_cliente(request):
    clientes = Cliente.objects.order_by('apellido')
    template = loader.get_template('display_clientes.html')
    return HttpResponse(template.render({'clientes': clientes}, request))

def index_autos(request):
    autos = Auto.objects.order_by('modelo')
    template = loader.get_template('index_autos.html')
    return HttpResponse(template.render({'autos': autos}, request))

def display_autos(request, autos_id):
    auto = get_object_or_404(Auto, pk=autos_id)
    template = loader.get_template('display_autos.html')
    context = {
        'auto': auto
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

def detalle_venta(request, venta_id):
    # Obtener la venta específica por su ID
    venta = get_object_or_404(Venta, pk=venta_id)
    
    # Calcular el valor total a pagar (asumiendo que IVA es un porcentaje)
    iva_porcentaje = venta.iva  # Si `iva` es un campo con porcentaje
    valor_auto = venta.valordelauto
    valortotalapagar = valor_auto + (valor_auto * iva_porcentaje / 100)
    
    # Preparar el contexto para la plantilla
    context = {
        'venta': venta,
        'valortotalapagar': valortotalapagar,
    }
    
    # Renderizar la plantilla con el contexto
    return render(request, 'detalle_venta.html', context)
