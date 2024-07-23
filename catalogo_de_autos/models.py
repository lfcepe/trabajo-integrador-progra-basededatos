from django.db import models

# Create your models here.

class Catalogos(models.Model):
    catalogo = models.CharField(max_length=100, null = True)
    item = models.CharField(max_length=50, null=True)
    valor = models.FloatField(max_length=(5), null=True)
    idraiz = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f'{self.catalogo} {self.item}'
    
    def ret_valor (self) -> float:
        return {self.valor}
    
class clientes(models.Model):
    apellidos = models.CharField(max_length= 20, null = False)
    nombres = models.CharField(max_length=20, null = False) 
    cedula = models.CharField(max_length=10, null = False)
    idprovincia = models.ForeignKey(Catalogos, on_delete=models.CASCADE)
    numerodetelefono = models.CharField(max_length=10, null= False)
    email = models.EmailField( max_length=100, null = False)
    idestadocliente = models.ForeignKey(Catalogos, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.apellidos} {self.nombres} {self.cedula} {self.numerodetelefono} {self.email}' 