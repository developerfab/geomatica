from django.shortcuts import render

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
	contexto = { "title":"BogoGIS-Notificacion", "latitud": 4.6282536, "longitud": -74.0657988 }
	return render(request, 'map_location.html', contexto)

def add_hueco(request):
	"""
	Metodo para agregar y crear una notificacion de hueco
	"""
	contexto = { 'title':'BogoGIS-huecos'}
	return render(request, 'enviar_hueco.html', contexto)