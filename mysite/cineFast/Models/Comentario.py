from django.db import models
from django.utils import timezone
from cineFast.Models.Filme import Filme

class Comentario(models.Model):
	texto = models.TextField(verbose_name='Comentário')
	data = models.DateTimeField(default=timezone.now,blank=True, null=False, verbose_name='Data')
	filme = models.ForeignKey(Filme)


	def dadosJSON(self):
		data = [{
			'TipoDado': 'Comentarios',
			'texto': self.texto,
			'data': str(self.data)
		}]
		return data