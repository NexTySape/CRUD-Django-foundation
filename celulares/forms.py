#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import celulares

class celularesForm(forms.ModelForm):
	idprod = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese código producto'}))
	ce_marca = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese Marca'}))
	ce_model = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese Modelo'}))
	ce_desc = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese Descripción'}))
	class Meta:
		model = celulares
		fields = ['idprod','ce_marca','ce_model','ce_desc']
