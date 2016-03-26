from django.db import models

class Ator(models.Model):

	nome = models.CharField(max_length=150, null=False, verbose_name='Nome')
	caminho_foto = models.CharField(max_length=100, null=True, verbose_name='Foto')

	def __str__(self):
		return self.nome

	def dadosJSON(self):

		data  = [{'nome': self.nome , 'caminho_foto': self.caminho_foto}]
		
		return data