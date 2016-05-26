#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import compras
from clientes.models import clientes
from celulares.models import celulares

class comprasForm(forms.ModelForm):

	f_compra = forms.DateField(widget=forms.DateInput(attrs={'class': 'error','placeholder': 'Ingrese Fecha'}))
	c_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese Numero Asignado'}))
	c_dni = forms.ModelChoiceField( queryset = clientes.objects.all() )
	ce_idprod = forms.ModelChoiceField( queryset = celulares.objects.all() )

	class Meta:
		model = compras
		fields = ['c_dni','ce_idprod','f_compra','c_num']
