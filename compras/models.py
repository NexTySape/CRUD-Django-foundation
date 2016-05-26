from __future__ import unicode_literals

from django.db import models
from clientes.models import clientes
from celulares.models import celulares

# Create your models here.
class compras(models.Model):
    c_dni = models.ForeignKey(clientes, null=True)
    ce_idprod = models.ForeignKey(celulares, null=True)
    f_compra = models.DateTimeField(blank=True)
    c_num = models.CharField(max_length=10)

    def __str__(self):
        return str(self.c_dni)
