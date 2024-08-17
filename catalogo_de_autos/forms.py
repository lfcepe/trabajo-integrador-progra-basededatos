from django import forms
from .models import ColorAuto,TipoCarro, Marca,FormaPago,Cliente,Auto,Venta


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
        fields = ['marca', 'tipodeauto', 'color', 'modelo', 'anioauto', 'precioporunidad', 'tipocombustible', 'codigoproducto', 'picture']


class Venta_Form (forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'auto', 'formadepago', 'cantidaddeventa', 'iva', 'valoriva', 'codigoventa']
        witgets = {
            'fechacompra': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
        }
        

        def save(self, commit = True):
            venta = super().save(commit=False)
            venta.obtener_valor_vehiculo()
            venta.calcular_costo_final()
            if commit:
                venta.save()
            return venta