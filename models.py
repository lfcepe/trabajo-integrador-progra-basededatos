# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autos(models.Model):
    idmarca = models.ForeignKey('Catalogos', models.DO_NOTHING, db_column='idmarca')
    idtipodeauto = models.ForeignKey('Catalogos', models.DO_NOTHING, db_column='idtipodeauto', related_name='autos_idtipodeauto_set')
    idcolor = models.ForeignKey('Catalogos', models.DO_NOTHING, db_column='idcolor', related_name='autos_idcolor_set')
    modelo = models.CharField()
    anioauto = models.CharField(max_length=4)
    precioporunidad = models.TextField()  # This field type is a guess.
    cantidad = models.IntegerField(blank=True, null=True)
    idestado = models.IntegerField()
    idtipocombustible = models.ForeignKey('Catalogos', models.DO_NOTHING, db_column='idtipocombustible', related_name='autos_idtipocombustible_set')
    codigoproducto = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'autos'


class Catalogos(models.Model):
    catalogo = models.CharField(max_length=50, blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    valor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idraiz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogos'


class Clientes(models.Model):
    apellidos = models.CharField(max_length=20)
    nombres = models.CharField(max_length=20)
    cedula = models.CharField(max_length=10)
    idprovincia = models.ForeignKey(Catalogos, models.DO_NOTHING, db_column='idprovincia')
    numerodetelefono = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    idestadocliente = models.ForeignKey(Catalogos, models.DO_NOTHING, db_column='idestadocliente', related_name='clientes_idestadocliente_set')

    class Meta:
        managed = False
        db_table = 'clientes'


class Kardex(models.Model):
    idauto = models.ForeignKey(Autos, models.DO_NOTHING, db_column='idauto')
    fechacantidadentrada = models.DateField()
    cantidaddeentrada = models.IntegerField()
    valorunitarioentrada = models.TextField()  # This field type is a guess.
    valortotalentrada = models.TextField()  # This field type is a guess.
    cantidadsalida = models.IntegerField(blank=True, null=True)
    valorunitariodesalida = models.TextField(blank=True, null=True)  # This field type is a guess.
    valortotaldesalida = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'kardex'


class Ventas(models.Model):
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    idauto = models.ForeignKey(Autos, models.DO_NOTHING, db_column='idauto')
    fechacompra = models.DateField()
    idformadepago = models.ForeignKey(Catalogos, models.DO_NOTHING, db_column='idformadepago')
    cantidaddeventa = models.IntegerField()
    valordelauto = models.TextField()  # This field type is a guess.
    idiva = models.ForeignKey(Catalogos, models.DO_NOTHING, db_column='idiva', related_name='ventas_idiva_set')
    valortotalapagar = models.TextField(blank=True, null=True)  # This field type is a guess.
    codigoventa = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'ventas'
