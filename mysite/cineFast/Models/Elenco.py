from django.db import models
from cineFast.Models.Diretor import Diretor
from cineFast.Models.Ator import Ator
import json

class Elenco(models.Model):
	
	descricao = models.CharField(max_length=100, verbose_name='Descrição')
	diretores = models.ManyToManyField(Diretor)
	atores = models.ManyToManyField(Ator)

	def __str__(self):
		return self.descricao

	def dadosJSON(self):

		diretores = [val for val in Diretor.objects.all() if val in self.diretores.all()]
		atores = [val for val in Ator.objects.all() if val in self.atores.all()]

		jsonDiretorStr = []
		jsonAtorStr = []
		for d in diretores:
			jsonDiretorStr += Diretor.dadosJSON(d)

		for a in atores:
			jsonAtorStr += Ator.dadosJSON(a)		

		data = [
			{
				'descricao': self.descricao,
				'diretores': jsonDiretorStr,
				'atores': jsonAtorStr	
			}
		]

		return data
