from django.db import models

class Diretor(models.Model):

	nome = models.CharField(max_length=150, verbose_name='Nome', null=False)
	caminho_foto = models.CharField(max_length=100, verbose_name='Foto', null=True)

	def __str__(self):
		return self.nome

	def dadosJSON(self):

		data  = [{'nome': self.nome , 'caminho_foto': self.caminho_foto}]
		
		return data