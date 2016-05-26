from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import compras
from clientes.models import clientes
from celulares.models import celulares
from .forms import comprasForm

def inicio(request):
    Compras = compras.objects.all()
    Clientes = clientes.objects.all()
    Celulares = celulares.objects.all()
    return render(request, 'inicio.html', {'Clientes': Clientes, 'Celulares': Celulares, 'Compras': Compras})

def comprasCreation(request, template='comprasForm.html'):
    form = comprasForm()
    if request.method == "POST":
        form = comprasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'comprasNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def comprasList(request):
    Compras = compras.objects.all()
    return render(request, 'comprasListado.html', {'Compras': Compras})

def comprasDetail(request, id, template='comprasDetalle.html'):
    Compras = get_object_or_404(compras, pk=id)
    return render_to_response(template, {'Compras': Compras}, context_instance=RequestContext(request))

def comprasDelete(request, id_c_dni):
    instance = get_object_or_404(compras, c_dni=id_c_dni)
    instance.delete()
    Compras = compras.objects.all()
    return render(request, 'comprasListado.html', {'Compras': Compras})

def comprasUpdate(request, id_c_dni):
    instance = get_object_or_404(compras, c_dni=id_c_dni)
    form = comprasForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Compras = compras.objects.all()
            return render(request, 'comprasListado.html', {'Compras': Compras})
    return render(request, 'comprasDetalle.html', {'form': form})


# Create your views here.
