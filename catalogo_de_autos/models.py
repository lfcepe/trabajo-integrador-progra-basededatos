from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone

class Marca(models.Model):
    marcaauto = models.CharField(max_length=50, null = False)

    def __str__(self) -> str:
        return self.marcaauto
    
class ColorAuto(models.Model):
    colorauto = models.CharField(max_length=50, null = False)

    def __str__(self):
        return self.colorauto
    

class TipoCarro(models.Model):
    modelocarro = models.CharField(max_length=50, null = False)
    
    def __str__(self) -> str:
        return self.modelocarro
      

class FormaPago(models.Model):
    formadepago = models.CharField(max_length=50, null = False)

    def __str__(self):
        return self.formadepago
    

class Cliente(models.Model):
    apellidos = models.CharField(max_length=20, null=False)
    nombres = models.CharField(max_length=20, null=False)
    cedula = models.CharField(max_length=10, null=False)
    PROVINCIAS= {
        ('AZ', 'AZUAY'),
	    ('BO', 'BOLIVAR'),
		('CÑ', 'CAÑAR'),
		('CA', 'CARCHI'),
		('CP', 'COTOPAXI'),
		('CB', 'CHIMBORAZO'),
	    ('EO', 'EL ORO'),
		('ES', 'ESMERALDAS'),
		('GY', 'GUAYAS'),
		('IB', 'IMBABURA'),
		('LJ', 'LOJA'),
		('LR', 'LOS RIOS'),
		('MN', 'MANABI'),
		('MS', 'MORONA SANTIAGO'),
		('NP', 'NAPO'),
		('PZ', 'PASTAZA'),
		('PC', 'PICHINCHA'),
		('TU', 'TUNGURAHUA'),
		('ZC', 'ZAMORA CHINCHIPE'),
		('GG', 'GALAPAGOS'),
		('SB', 'SUCUMBIOS'),
		('OR', 'ORELLANA'),
		('SD', 'SANTO DOMINGO DE LOS TSACHILAS'),
		('SE', 'SANTA ELENA'),
    }
    provincia = models.CharField(choices= PROVINCIAS, null=False)
    numerodetelefono = models.CharField(max_length=10, null = False)
    email = models.CharField(max_length=80, null = False)
    ESTADO_CLIENTE = {
        ('AC', 'ACTIVO'),
        ('INAC', 'INACTIVO'),
    }
    estadocliente = models.CharField(choices= ESTADO_CLIENTE, null = False)

    def __str__(self):
        return f'{self.apellidos} {self.nombres}'
    

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipodeauto = models.ForeignKey(TipoCarro, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorAuto, on_delete=models.CASCADE)
    modelo = models.CharField(null = False)
    anioauto = models.CharField(max_length=4, null = False)
    precioporunidad = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null = False)
    cantidad = models.IntegerField(default=0, null = False)
    ESTADO_PRODUCTO = {
        ('EN STOCK','EN STOCK'),
        ('SIN STOCK', 'SIN STOCK')
    }
    estado = models.CharField(default='SIN STOCK' ,choices= ESTADO_PRODUCTO, null=False)
    COMBUSTIBLE = {
        ('DIESEL', 'DIESEL'),
        ('SUPER/EXTRA', 'SUPER/EXTRA'),
    }
    tipocombustible = models.CharField(max_length=50, choices= COMBUSTIBLE, null=False)
    codigoproducto = models.CharField(max_length=7)
    picture = models.ImageField(upload_to='cars_images')

    def __str__(self):
        return f'{self.tipodeauto} {self.marca} {self.modelo}'
        

class KardexEntradas(models.Model):
    auto = models.CharField(max_length=50, null = False)
    fechacantidadentrada = models.DateField(null = False)
    cantidaddeentrada = models.IntegerField(null = False)
    valorunitarioentrada = MoneyField (max_digits=14, decimal_places=2, default_currency='USD', null = False)
    valortotalentrada = MoneyField (max_digits=14, decimal_places=2, default_currency='USD', null = False)

    def __str__(self):
        return self.auto
     
class KardexSalidas(models.Model):
    auto = models.CharField(max_length=50, null = False)
    fechacantidaddesalida = models.DateField(null = True)
    cantidadsalida = models.IntegerField(null=True)
    valorunitariodesalida = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null=True)  
    valortotaldesalida = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null=True) 

    def __str__(self):
        return self.auto

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fechacompra = models.DateField(default=timezone.now, null = False)
    formadepago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    cantidaddeventa = models.IntegerField(null = False)
    valordelauto = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null= False) 
    iva = models.CharField(default="15%", max_length=3, null = False)
    valoriva = models.DecimalField(max_digits=5, decimal_places=2, null = False)
    valortotalapagar = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null= False) 
    codigoventa = models.CharField(max_length=7, null = False)

    def __str__(self) -> str:
        return f'{self.codigoventa}-{self.cliente}'
    
    def obtener_valor_vehiculo(self):
        self.valordelauto = self.auto.precioporunidad
        return self.valordelauto
    
    def calcular_costo_final (self):
        if self.cantidaddeventa <= self.auto.cantidad:
            auto = self.auto.precioporunidad
            cantidad = self.cantidaddeventa
            self.valortotalapagar = cantidad * auto * self.valoriva
            return self.valortotalapagar
        else:
            return print('Cantidad de venta mayor a la cantidad de stock, vuelva a ingresar')
    
    def save(self, *args, **kwargs):
        if not self.valordelauto:
            self.obtener_valor_vehiculo()
        if not self.valortotalapagar:
            self.calcular_costo_final()
        super().save(*args, **kwargs)


class TotalCompras(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    total_compras = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    fecha = models.DateField(auto_now=True)

    def actualizar_total(self):
        total = Venta.objects.filter(cliente=self.cliente).aggregate(total=models.Sum('valortotalapagar'))['total'] or 0.00
        self.total_compras = total
        self.save()