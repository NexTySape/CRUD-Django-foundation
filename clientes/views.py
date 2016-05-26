from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import clientes
from celulares.models import celulares
from compras.models import compras
from .forms import clientesForm

def inicio(request):
    Clientes = clientes.objects.all()
    Celulares = celulares.objects.all()
    Compras = compras.objects.all()

    return render(request, 'inicio.html', {'Clientes': Clientes, 'Celulares': Celulares, 'Compras': Compras})

def clientesCreation(request, template='clientesForm.html'):
    form = clientesForm()
    if request.method == "POST":
        form = clientesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'clientesNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def clientesList(request):
    Clientes = clientes.objects.all()
    return render(request, 'clientesListado.html', {'Clientes': Clientes})

def clientesDetail(request, id, template='clientesDetalle.html'):
    Clientes = get_object_or_404(clientes, pk=id)
    return render_to_response(template, {'Clientes': Clientes}, context_instance=RequestContext(request))

def clientesDelete(request, id_dni):
    instance = get_object_or_404(clientes, dni=id_dni)
    instance.delete()
    Clientes = clientes.objects.all()
    return render(request, 'clientesListado.html', {'Clientes': Clientes})

def clientesUpdate(request, id_dni):
    instance = get_object_or_404(clientes, dni=id_dni)
    form = clientesForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Clientes = clientes.objects.all()
            return render(request, 'clientesListado.html', {'Clientes': Clientes})
    return render(request, 'clientesDetalle.html', {'form': form})


# Create your views here.
