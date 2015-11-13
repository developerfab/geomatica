from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Ventana principal
    """
    contexto = {}
    return render(request, 'index.html', contexto)
