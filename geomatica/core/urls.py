from django.conf.urls import patterns, url
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
    url(r'^lista_notificacion/$', views.lista_notificacion, name="lista_notificacion"),
    url(r'^add_hueco/$', views.add_hueco, name="enviar_notificacion_hueco"),
    url(r'^opcion_hueco/$', views.opcion_hueco, name="opcion_hueco"),
    url(r'^especifico_notificacion/$', views.especifico_notificacion, name="especifico_notificacion"),
    url(r'^estadisticas_hueco/$', views.estadistica_hueco, name="estadisticas_hueco"),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)