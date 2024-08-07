from django.db import models
from djmoney.models.fields import MoneyField

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
    
class Iva(models.Model):
    porcentajeiva = models.CharField(max_length = 4, null = False)
    valordecalculo = models.DecimalField(max_digits=4, decimal_places=2, null = False)

    def __str__(self):
        return self.porcentajeiva
    

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
    cantidad = models.IntegerField(null=True)
    ESTADO_PRODUCTO = {
        ('SCK','EN STOCK'),
        ('SSCK', 'SIN STOCK')
    }
    estado = models.CharField(default="SIN STOCK", choices= ESTADO_PRODUCTO, null=False)
    COMBUSTIBLE = {
        ('DS', 'DIESEL'),
        ('S/E', 'SUPER/EXTRA'),
    }
    tipocombustible = models.CharField(max_length=50, choices= COMBUSTIBLE, null=False)
    codigoproducto = models.CharField(max_length=7, null=False)
    imagencarro = models.ImageField(upload_to='imagenes_autos')

    def __str__(self):
        return f'{self.tipodeauto} {self.marca} {self.modelo}'
        

class Kardex(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fechacantidadentrada = models.DateField(null = False)
    cantidaddeentrada = models.IntegerField(null = False)
    valorunitarioentrada = MoneyField (max_digits=14, decimal_places=2, default_currency='USD', null = False)
    valortotalentrada = MoneyField (max_digits=14, decimal_places=2, default_currency='USD', null = False)
    fechacantidaddesalidad = models.DateField(null = True)
    cantidadsalida = models.IntegerField(null=True)
    valorunitariodesalida = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null=True)  
    valortotaldesalida = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null=True) 

    def __str__(self):
        return self.auto
     

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fechacompra = models.DateField(null = False)
    formadepago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    cantidaddeventa = models.IntegerField(null = False)
    valordelauto = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null= False) 
    iva = models.ForeignKey(Iva,on_delete=models.CASCADE)
    valortotalapagar = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null= False) 
    codigoventa = models.CharField(max_length=7, null = False)
