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

def lista_notificacion(request):
	"""
	Metodo para visualizar la lista de notificaciones
	"""
	lista = Hueco.objects.all()
	contexto = { "title":"BogoGIS-Notificacion", "lista":lista }
	return render(request, 'lista_notificacion.html', contexto)

def opcion_hueco(request):
	contexto = { "title":"BogoGIS-adicionar" }
	return render(request, 'enviar_hueco.html', contexto)

def add_hueco(request):
	"""
	Metodo para agregar y crear una notificacion de hueco
	"""
	contexto = { 'title':'BogoGIS-huecos'}
	msg = ""
	if request.method == 'POST':
		form = FormCoord(request.POST)
		if form.is_valid():
			form.save()
			msg = "Tu informacion es valiosa para nosostros, gracias por notificar"
		else:
			msg = "Error en la informacion, por favor revisa los campos"
			contexto['form'] = form
	else:
		form = FormCoord()
		contexto['form'] = form
	contexto['msg'] = msg
	return render(request, 'from_coord.html', contexto)

def especifico_notificacion(request):
	"""
	Metodo que permite ver de forma espeficica una notificacion
	"""
	notificacion = Hueco.objects.get(id=request.GET['identificador'])
	contexto = { "title":"Notificacion Espeficica", "latitud": notificacion.latitud, "longitud": notificacion.longitud }
	return render(request, 'map_location.html', contexto)
