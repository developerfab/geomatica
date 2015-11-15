from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
    url(r'^notificacion/$', views.notificacion, name="notificacion"),
    url(r'^add_hueco/$', views.add_hueco, name="enviar_notificacion_hueco"),
    )