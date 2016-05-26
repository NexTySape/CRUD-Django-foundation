from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import celulares
from clientes.models import clientes
from compras.models import compras
from .forms import celularesForm

def inicio(request):
    Celulares = celulares.objects.all()
    Clientes = clientes.objects.all()
    Compras = compras.objects.all()
    return render(request, 'inicio.html', {'Clientes': Clientes, 'Celulares': Celulares, 'Compras': Compras})

def celularesCreation(request, template='celularesForm.html'):
    form = celularesForm()
    if request.method == "POST":
        form = celularesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'celularesNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def celularesList(request):
    Celulares = celulares.objects.all()
    return render(request, 'celularesListado.html', {'Celulares': Celulares})

def celularesDetail(request, id, template='celularesDetalle.html'):
    Celulares = get_object_or_404(celulares, pk=id)
    return render_to_response(template, {'Celulares': Celulares}, context_instance=RequestContext(request))

def celularesDelete(request, id_idprod):
    instance = get_object_or_404(celulares, idprod=id_idprod)
    instance.delete()
    Celulares = celulares.objects.all()
    return render(request, 'celularesListado.html', {'Celulares': Celulares})

def celularesUpdate(request, id_idprod):
    instance = get_object_or_404(celulares, idprod=id_idprod)
    form = celularesForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Celulares = celulares.objects.all()
            return render(request, 'celularesListado.html', {'Celulares': Celulares})
    return render(request, 'celularesDetalle.html', {'form': form})

# Create your views here.
