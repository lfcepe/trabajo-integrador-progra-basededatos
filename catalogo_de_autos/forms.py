from django import forms
from .models import ColorAuto,TipoCarro,Iva,Marca,FormaPago,Cliente,Auto,Kardex,Venta
from djmoney.forms.widgets import MoneyWidget

class Marca_Form(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'marcaauto': forms.TextInput(attrs={'class': 'form_control'}),
        }

class ColorAuto_Form(forms.ModelForm):
    class Meta:
        model = ColorAuto
        fields = '__all__'
        widgets = {
            'colorauto': forms.TextInput(attrs={'class': 'form_control'}),
        }

class TipoCarro_Form(forms.ModelForm):
    class Meta:
        model = TipoCarro
        fields = '__all__'
        widgets = {
            'modelocarro': forms.TextInput(attrs={'class': 'form_control'}),
        }

class Iva_Form(forms.ModelForm):
    class Meta:
        model = Iva
        fields = '__all__'
        widgets = {
            'porcentajeiva': forms.TextInput(attrs={'class': 'form_control'}),
            'valordecalculo': forms.NumberInput(attrs={'class': 'form_control'}),
        }

class FormaPago_Form(forms.ModelForm):
    class Meta:
        model = FormaPago
        fields = '__all__'
        widgets = {
            'formadepago': forms.TextInput(attrs={'class': 'form_control'}),
        }

class Cliente_Form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'apellidos': forms.TextInput(attrs={'class': 'form_control'}),
            'nombres': forms.TextInput(attrs={'class': 'form_control'}),
            'cedula': forms.TextInput(attrs={'class': 'form_control'}),
            'provincia': forms.Select(attrs={'class': 'form_control'}),
            'numerodetelefono': forms.TextInput(attrs={'class': 'form_control'}),
            'email': forms.TextInput(attrs={'class': 'form_control'}),
            'estadocliente': forms.Select(attrs={'class': 'form_control'}),
        }

class Auto_Form(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'tipodeauto', 'color', 'modelo', 'anioauto', 'precioporunidad', 'estado', 'tipocombustible', 'codigoproducto', 'imagencarro'
]
        widgets = {
            'marca': forms.Select(attrs={'class': 'form_control'}),
            'tipodeauto': forms.Select(attrs={'class': 'form_control'}),
            'color': forms.Select(attrs={'class': 'form_control'}),
            'modelo': forms.TextInput(attrs={'class': 'form_control'}),
            'anioauto': forms.TextInput(attrs={'class': 'form_control'}),
            'precioporunidad': MoneyWidget(amount_widget=forms.NumberInput(attrs={'class': 'form-control'}), currency_widget=forms.Select(attrs={'class': 'form-control'})),
            'estado': forms.Select(attrs={'class': 'form_control'}),
            'tipocombustible': forms.Select(attrs={'class': 'form_control'}),
            'codigoproducto': forms.Select(attrs={'class': 'form_control'}),
            'imagencarro': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class Kardex_Form (forms.ModelForm):
    class Meta:
        model = Kardex
        fields = ['auto', 'fechacantidadentrada', 'cantidaddeentrada']
        widgets = {
            'auto': forms.Select(attrs={'class': 'form_control'}),
            'fechacantidadentrada': forms.DateInput(attrs={'type': 'date'}),
            'cantidaddeentrada': forms.NumberInput(attrs={'class': 'form_control'}),
        }

class Venta_Form (forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'auto', 'fechacompra', 'formadepago', 'cantidaddeventa', 'iva', 'codigoventa']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form_control'}),
            'auto': forms.Select(attrs={'class': 'form_control'}),
            'fechacompra': forms.DateInput(attrs={'type': 'date'}),
            'formadepago': forms.Select(attrs={'class': 'form_control'}),
            'cantidaddeventa': forms.NumberInput(attrs={'class': 'form_control'}),
            'iva': forms.Select(attrs={'class': 'form_control'}),
            'codigoventa': forms.TextInput(attrs={'class': 'form_control'}),
        }