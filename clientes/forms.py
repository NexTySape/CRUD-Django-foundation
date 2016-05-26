#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import clientes

class clientesForm(forms.ModelForm):
	dni = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese dni cliente'}))
	c_nomb = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese nombre'}))
	c_telf = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrece número de contacto'}))
	c_dir = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese dirección'}))
	class Meta:
		model = clientes
		fields = ['dni','c_nomb','c_telf','c_dir']
