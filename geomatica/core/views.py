from django.shortcuts import render
from core.models import *
from core.forms import FormCoord

# Create your views here.

def index(request):
    """
    Ventana principal
    """
    contexto = {'title':'BogoGIS'}
    return render(request, 'index.html', contexto)

def notificacion(request):
	"""
	Metodo para visualizar la lista de notificaciones
	"""
	contexto = { "title":"BogoGIS-Notificacion", "latitud": 4.710988599999999, "longitud": -74.072092 }
	return render(request, 'map_location.html', contexto)

def opcion_hueco(request):
	contexto = { "title":"BogoGIS-adicionar" }
	return render(request, 'enviar_hueco.html', contexto)

def add_hueco(request):
	"""
	Metodo para agregar y crear una notificacion de hueco
	"""
	contexto = { 'title':'BogoGIS-huecos'}
	if request.method == 'POST':
		return render(request, 'enviar_hueco.html', contexto)
	else:
		form = FormCoord()
		contexto['form'] = form

	return render(request, 'from_coord.html', contexto)
