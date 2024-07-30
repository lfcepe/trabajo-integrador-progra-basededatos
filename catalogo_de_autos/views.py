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

def index_kardex(request):
    kardexs = Kardex.objects.order_by('fechacantidadentrada')
    template = loader.get_template('index_kardex.html')
    return HttpResponse(template.render({'kardexs': kardexs}, request))


def obtener_kardex(kardex_id):
    kardex = Kardex.objects.get(pk = kardex_id)
    return {'kardex': kardex}

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
