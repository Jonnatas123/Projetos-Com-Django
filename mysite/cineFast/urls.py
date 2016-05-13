from django.conf.urls import include, url
from cineFast import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^inserir_comentario$', views.inserir_comentario),
    url(r'^listar_comentario$', views.listar_comentario),
    url(r'^remover_comentario$', views.remover_comentario),
    url(r'^inserir_diretor$', views.inserir_diretor, name="form"),
    url(r'^listar_diretor$', views.listar_diretor),
    url(r'^remover_diretor$', views.remover_diretor, name="id_diretor"),
]