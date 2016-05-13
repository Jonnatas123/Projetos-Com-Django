from django.db import models

class Diretor(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=150, verbose_name='Nome', null=False)
	foto = models.ImageField(upload_to='imagens\diretores', null=True)

	def __str__(self):
		return self.nome

	def dadosJSON(self):
		try:
			if(self.foto != 'null'):
				caminho = str(self.foto.path).replace('C:\Program Files (x86)\EasyPHP-Devserver-16.1\eds-www', '')
				print(caminho)
				data  = [{'id': self.id, 'nome': self.nome , 'caminho_foto': caminho}]
			else:
				data  = [{'id': self.id, 'nome': self.nome , 'caminho_foto': ''}]
			return data
		except Exception as e:
			print(e)
			return [{'id': self.id, 'nome': self.nome}]
