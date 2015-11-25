from django.shortcuts import render
from core.models import *
from core.forms import FormCoord, FormRobo

# Create your views here.

def index(request):
    """
    Ventana principal
    """
    contexto = {'title':'Hollow Street'}
    return render(request, 'index.html', contexto)

def lista_notificacion(request):
    """
    Metodo para visualizar la lista de notificaciones
    """
    lista = Hueco.objects.all()
    contexto = { "title":"Hollow-Notificacion", "lista":lista }
    return render(request, 'lista_notificacion.html', contexto)

def opcion_hueco(request):
    contexto = { "title":"Hollow-adicionar" }
    return render(request, 'enviar_hueco.html', contexto)

def add_hueco(request):
    """
    Metodo para agregar y crear una notificacion de hueco
    """
    contexto = { 'title':'Hollow-huecos'}
    msg = ""
    if request.method == 'POST':
        form = FormCoord(request.POST, request.FILES)
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


def estadistica_hueco(request):
    """
    Este metodo se encarga de realizar las estadisticas para los huecos
    """
    if request.method == 'GET':
        seleccion = Hueco.objects.get(id=request.GET['identificador'])
        notificacion = Hueco.objects.filter(latitud = seleccion.latitud, longitud=seleccion.longitud)
        contexto = { "title":"Notificacion Espeficica", "latitud": notificacion[0].latitud, "longitud": notificacion[0].longitud, "cantidad":255-len(notificacion)}
    return render(request, 'estadisticas_hueco.html', contexto)

def reportar_robo(request):
    """
    Este metodo permite reportar un robo
    """
    contexto = { 'title': 'Hollow-huecos' }
    msg = ""
    if request.method == 'POST':
        form = FormRobo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = "Tu informacion es valiosa para nosostros, gracias por notificar"
        else:
            msg = "Error en la informacion, por favor revisa los campos"
            contexto['form'] = form
    else:
        form = FormRobo()
        contexto['form'] = form
    contexto['msg'] = msg
    return render(request, 'form_robo.html', contexto)
