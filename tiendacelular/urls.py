"""tiendacelular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'clientes.views.inicio', name='inicio'),

    url(r'^clientes/nuevo/$','clientes.views.clientesCreation' , name='clientes_nuevo'),
    url(r'^clientes/listado/$','clientes.views.clientesList' , name='clientes_listado'),
    url(r'^cliente/(?P<id_dni>\d+)$','clientes.views.clientesUpdate', name='cliente_detalle'),
    url(r'^cliente_e/(?P<id_dni>\d+)$','clientes.views.clientesDelete', name='cliente_borrar'),

    url(r'^celulares/nuevo/$','celulares.views.celularesCreation' , name='celulares_nuevo'),
    url(r'^celulares/listado/$','celulares.views.celularesList' , name='celulares_listado'),
    url(r'^celular/(?P<id_idprod>\d+)$','celulares.views.celularesUpdate', name='celular_detalle'),
    url(r'^celular_e/(?P<id_idprod>\d+)$','celulares.views.celularesDelete', name='celular_borrar'),

    url(r'^compras/nuevo/$','compras.views.comprasCreation', name='compras_nuevo'),
    url(r'^compras/listado/$','compras.views.comprasList', name='compras_listado'),
    url(r'^compra/(?P<id_c_dni>\d+)$','compras.views.comprasUpdate', name='compra_detalle'),
    url(r'^compra_e/(?P<id_c_dni>\d+)$','compras.views.comprasDelete', name='compra_borrar'),
)
