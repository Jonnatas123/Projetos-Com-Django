from django.db import models
from django.utils import timezone
from cineFast.Models.Filme import Filme

class Comentario(models.Model):
	id = models.AutoField(primary_key=True)
	texto = models.TextField(verbose_name='Comentário')
	data = models.DateTimeField(default=timezone.now,blank=True, null=False, verbose_name='Data')
	filme = models.ForeignKey(Filme)


	def dadosJSON(self):
		data = [{
			'TipoDado': 'Comentarios',
			'id': self.id,
			'texto': self.texto,
			'data': str(self.data)
		}]
		return data