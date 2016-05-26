from __future__ import unicode_literals

from django.db import models

# Create your models here.
class clientes(models.Model):
    dni = models.AutoField(primary_key=True)
    c_nomb = models.CharField(max_length=20)
    c_telf = models.CharField(max_length=10)
    c_dir = models.CharField(max_length=15)

    def __str__(self):
        return str(self.dni)

    #def __unicode__(self):
    #    return self.dni
