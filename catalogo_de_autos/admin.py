from django.contrib import admin
from .models import Marca, TipoCarro, ColorAuto, FormaPago, Cliente, Auto, KardexEntradas, KardexSalidas, Venta
# Register your models here.

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoCarro)
class TipoCarroAdmin(admin.ModelAdmin):
    pass

@admin.register(ColorAuto)
class ColorAutoAdmin(admin.ModelAdmin):
    pass


@admin.register(FormaPago)
class FormaPagoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    pass

@admin.register(KardexEntradas)
class KardexAdmin(admin.ModelAdmin):
    pass

@admin.register(KardexSalidas)
class KardexAdmin(admin.ModelAdmin):
    pass

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    pass