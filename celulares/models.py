from __future__ import unicode_literals

from django.db import models

# Create your models here.
class celulares(models.Model):
    idprod = models.AutoField(primary_key=True)
    ce_marca = models.CharField(max_length=15)
    ce_model = models.CharField(max_length=13)
    ce_desc = models.CharField(max_length=30)


    def __str__(self):
        return str(self.idprod)
