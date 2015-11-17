from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
    url(r'^lista_notificacion/$', views.lista_notificacion, name="lista_notificacion"),
    url(r'^add_hueco/$', views.add_hueco, name="enviar_notificacion_hueco"),
    url(r'^opcion_hueco/$', views.opcion_hueco, name="opcion_hueco"),
    )