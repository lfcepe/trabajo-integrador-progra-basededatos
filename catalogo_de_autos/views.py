from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from .models import Marca, ColorAuto, TipoCarro, Iva, FormaPago, Cliente, Auto, Kardex, Venta
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import Marca_Form, ColorAuto_Form, TipoCarro_Form, Iva_Form, FormaPago_Form, Cliente_Form, Auto_Form, Kardex_Form, Venta_Form
# Create your views here.

def index(request):
    return render(request, 'index.html')

def index_categoria(request):
    return render(request, 'index_categorias.html')

def display_marca(request):
    marcas = Marca.objects.order_by('marcaauto')
    return render(request,'display_marca.html', {'marcas':marcas})

def display_colorauto(request):
    colores = ColorAuto.objects.order_by('colorauto')
    return render(request, 'display_colorauto.html', {'colores':colores})

    
def display_tipocarro(request):
    tipos = TipoCarro.objects.order_by('modelocarro')
    return render(request,'display_tipocarro.html', {'tipos':tipos})

def display_iva(request):
    piva = Iva.objects.order_by('valordecalculo')
    return render(request, 'display_iva.html', {'piva': piva})

    
def display_formapago(request):
    pagos = FormaPago.objects.order_by('formadepago')
    return render(request, 'display_formapago.html', {'pagos':pagos})


def index_cliente(request):
    clientes = Cliente.objects.order_by('apellidos')
    return render(request, 'index_clientes.html',{'clientes':clientes})

def index_autos(request):
    autos = Auto.objects.order_by('modelo')
    return render(request, 'index_autos.html',{'autos':autos})

def display_autos(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    return render(request, 'display_autos.html', {'auto':auto})

def index_kardex(request):
    kardexs = Kardex.objects.order_by('fechacantidadentrada')
    template = loader.get_template('index_kardex.html')
    return HttpResponse(template.render({'kardexs': kardexs}, request))


def obtener_kardex(kardex_id):
    kardex = Kardex.objects.get(pk = kardex_id)
    return {'kardex': kardex}

def index_ventas(request):
    ventas = Venta.objects.order_by('fechacompra')
    template = loader.get_template('index_ventas.html')
    return HttpResponse(template.render({'ventas': ventas}, request))

#LOGIN VIEW
class CustomLoginView(LoginView):
    template_name = 'login.html'

#ADD INFORMATION
@login_required
def add_marca(request):
    if request.method == 'POST':
        form = Marca_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:display_marca')
    else:
        form = Marca_Form()
    
    return render(request, 'marca_form.html', {'form': form})

@login_required
def add_colorauto(request):
    if request.method == 'POST':
        form = ColorAuto_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:display_colorauto')
    else:
        form = ColorAuto_Form()
    
    return render(request, 'colorauto_form.html', {'form': form})

@login_required
def add_tipocarro(request):
    if request.method == 'POST':
        form = TipoCarro_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:display_tipocarro')
    else:
        form = TipoCarro_Form()
    
    return render(request, 'tipodecarro_form.html', {'form': form})

@login_required
def add_iva(request):
    if request.method == 'POST':
        form = Iva_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:display_iva')
    else:
        form = Iva_Form()
    
    return render(request, 'iva_form.html', {'form': form})

@login_required
def add_formapago(request):
    if request.method == 'POST':
        form = FormaPago_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:display_formapago')
    else:
        form = FormaPago_Form()
    
    return render(request, 'formadepago_form.html', {'form': form})

@login_required
def add_cliente(request):
    if request.method == 'POST':
        form = Cliente_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_clientes')
    else:
        form = Cliente_Form()
    
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def add_auto(request):
    if request.method == 'POST':
        form = Auto_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_autos')
    else:
        form = Auto_Form()

    return render(request, 'auto_form.html', {'form': form})

@login_required
def add_kardex(request):
    if request.method == 'POST':
        form = Kardex_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_kardex')
    else:
        form = Kardex_Form()
    
    return render(request, 'kardex_form.html', {'form': form})

@login_required
def add_venta(request):
    if request.method == 'POST':
        form = Venta_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_ventas')
    else:
        form = Venta_Form()
    
    return render(request, 'venta_form.html', {'form': form})

#EDIT ELEMENTS
@login_required
def edit_marca(request, id):
    marca = get_object_or_404(Marca, pk = id)
    if request.method == 'POST':
        form = Marca_Form(request.POST,request.FILES, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_categorias')
    else:
        form = Marca_Form(instance=marca)
        
    return render(request, 'marca_form.html', {'form': form})

@login_required
def edit_colorauto(request, id):
    color = get_object_or_404(ColorAuto, pk = id)
    if request.method == 'POST':
        form = ColorAuto_Form(request.POST,request.FILES, instance=color)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_categorias')
    else:
        form = TipoCarro_Form(instance=color)
        
    return render(request, 'colorauto_form.html', {'form': form})

@login_required
def edit_tipocarro(request, id):
    tipo = get_object_or_404(TipoCarro, pk = id)
    if request.method == 'POST':
        form = TipoCarro_Form(request.POST,request.FILES, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_categorias')
    else:
        form = TipoCarro_Form(instance=tipo)
        
    return render(request, 'tipodecarro_form.html', {'form': form})

@login_required
def edit_iva(request, id):
    iva = get_object_or_404(Iva, pk = id)
    if request.method == 'POST':
        form = Iva_Form(request.POST,request.FILES, instance=iva)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_categorias')
    else:
        form = Iva_Form(instance=iva)
        
    return render(request, 'iva_form.html', {'form': form})

@login_required
def edit_formapago(request, id):
    pago = get_object_or_404(FormaPago, pk = id)
    if request.method == 'POST':
        form = Marca_Form(request.POST,request.FILES, instance=pago)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_categorias')
    else:
        form = FormaPago_Form(instance=pago)
        
    return render(request, 'formadepago_form.html', {'form': form})

@login_required
def edit_marca(request, id):
    marca = get_object_or_404(Marca, pk = id)
    if request.method == 'POST':
        form = Marca_Form(request.POST,request.FILES, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_categorias')
    else:
        form = Marca_Form(instance=marca)
        
    return render(request, 'marca_form.html', {'form': form})

@login_required
def edit_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk = id)
    if request.method == 'POST':
        form = Cliente_Form(request.POST,request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_clientes')
    else:
        form = Cliente_Form(instance=cliente)
        
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def edit_auto(request, id):
    auto = get_object_or_404(Auto, pk = id)
    if request.method == 'POST':
        form = Auto_Form(request.POST,request.FILES, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_autos')
    else:
        form = Auto_Form(instance=auto)
        
    return render(request, 'auto_form.html', {'form': form})

@login_required
def edit_kardex(request, id):
    kardex = get_object_or_404(Kardex, pk = id)
    if request.method == 'POST':
        form = Kardex_Form(request.POST,request.FILES, instance=kardex)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_kardex')
    else:
        form = Kardex_Form(instance=kardex)
        
    return render(request, 'kardex_form.html', {'form': form})

@login_required
def edit_venta(request, id):
    venta = get_object_or_404(Venta, pk = id)
    if request.method == 'POST':
        form = Venta_Form(request.POST,request.FILES, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('catalogo_de_autos:index_ventas')
    else:
        form = Venta_Form(instance=venta)
        
    return render(request, 'venta_form.html', {'form': form})

#DELETE ELEMENTS

@login_required
def delete_marca(request, id):
    marca = get_object_or_404(Marca, pk = id)
    marca.delete()
    return redirect("catalogo_de_autos:display_marca")

@login_required
def delete_colorauto(request, id):
    color = get_object_or_404(ColorAuto, pk = id)
    color.delete()
    return redirect("catalogo_de_autos:display_colorauto")

@login_required
def delete_tipocarro(request, id):
    tipo = get_object_or_404(TipoCarro, pk = id)
    tipo.delete()
    return redirect("catalogo_de_autos:display_tipocarro")

@login_required
def delete_iva(request, id):
    iva = get_object_or_404(Iva, pk = id)
    iva.delete()
    return redirect("catalogo_de_autos:display_iva")

@login_required
def delete_formapago(request, id):
    pago = get_object_or_404(FormaPago, pk = id)
    pago.delete()
    return redirect("catalogo_de_autos:display_formapago")

@login_required
def delete_clientes(request, id):
    cliente = get_object_or_404(Cliente, pk = id)
    cliente.delete()
    return redirect("catalogo_de_autos:index_clientes")

@login_required
def delete_autos(request, id):
    auto = get_object_or_404(Auto, pk = id)
    auto.delete()
    return redirect("catalogo_de_autos:index_autos")

@login_required
def delete_kardex(request, id):
    kardex = get_object_or_404(Kardex, pk = id)
    kardex.delete()
    return redirect("catalogo_de_autos:index_kardex")

@login_required
def delete_ventas(request, id):
    venta = get_object_or_404(Venta, pk = id)
    venta.delete()
    return redirect("catalogo_de_autos:index_ventas")