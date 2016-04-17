from django.shortcuts import render
from cineFast.Models.Filme import Filme
from cineFast.Models.Comentario import Comentario
import json
from django.http import HttpResponse

# Create your views here.
context_padrao = 'cineFast/src/'
def index(request):

	filmesLancamento = Filme.objects.all().order_by('-data_lancamento')[:3];
	filmesSinopse = Filme.objects.all().order_by('-data_lancamento')[3:7];

	data = []
	if(not filmesLancamento and not filmesSinopses):
		data = ['nenhum filme']
	else:
		for fl in filmesLancamento:
			data += Filme.dadosJSON(fl, 'filmesLancamento')

		for fs in filmesSinopse:
			data += Filme.dadosJSON(fs, 'filmesSinopse')

	return HttpResponse(json.dumps(data), content_type='application/json')

def inserir_comentario(request):
	filme = ''
	comentario = Comentario();
	comentario.texto = request.GET.get("comentario")

	if(int(request.GET.get("id_comentario")) == 0):
		filme = Filme.objects.get(titulo=request.GET.get("filme"))
		comentario.filme = filme
		comentario.save()
	else:
		id = request.GET.get("id_comentario");
		Comentario.objects.filter(pk=id).update(texto=comentario.texto)
	return HttpResponse(json.dumps('Ok'), content_type='application/json')

def listar_comentario(request):
	t = str(request.GET.get("filme")).replace("'", "")
	data = []
	try:

		filme = Filme.objects.get(titulo=t)
		comentarios = Comentario.objects.filter(filme__titulo=filme.titulo).order_by('-data')
		for c in comentarios:
			data += Comentario.dadosJSON(c)
	
	except Exception:
		return HttpResponse(json.dumps('Nenhum comentário'), content_type='application/json')  
	
	return HttpResponse(json.dumps(data), content_type='application/json')

def remover_comentario(request):
	print("Entrou")
	try:
		id = request.GET.get("id_comentario")
		c = Comentario.objects.get(id=id)
		c.delete()
	except Exception:
		print("Erro ao deletar comentário")
		return HttpResponse(json.dumps('Erro ao remover'), content_type='application/json')
	return HttpResponse(json.dumps('Sucesso ao remover'), content_type='application/json')
