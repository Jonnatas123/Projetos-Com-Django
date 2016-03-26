from django.db import models
from django.utils import timezone
from cineFast.Models.Elenco import Elenco


class Filme(models.Model):
	titulo  = models.CharField(max_length=50, verbose_name='Título')
	descricao = models.TextField(verbose_name='Descrição')
	data_lancamento = models.DateField(blank=True, null=False, verbose_name='Data de Lançamento')
	caminho_imagem = models.CharField(blank=True, null=True, max_length=100, verbose_name='Imagem')
	caminho_trailer = models.CharField(blank=True, null=True, max_length=100, verbose_name='Trailer')
	autor = models.ForeignKey('auth.User', null=True)
	elenco = models.ForeignKey(Elenco, null=True)
	em_cartaz = models.BooleanField(default=True, verbose_name='Em Cartaz')

	def __str__(self):
		return self.titulo

	def dadosJSON(self, tipo):
		data = [
			{ 
				'TipoDado': tipo,
				'titulo': self.titulo,
				'descricao': self.descricao,
				'data_lancamento': str(self.data_lancamento),
				'caminho_imagem': self.caminho_imagem,
				'caminho_trailer': self.caminho_trailer,
				#'autor': self.autor,
				'elenco': Elenco.dadosJSON(self.elenco),
				'em_cartaz': self.em_cartaz,
			}
		]

		return data

