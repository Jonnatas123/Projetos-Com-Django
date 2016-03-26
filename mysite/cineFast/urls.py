from django.conf.urls import include, url
from cineFast import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^inserir_comentario$', views.inserir_comentario),
    url(r'^listar_comentario$', views.listar_comentario),
]