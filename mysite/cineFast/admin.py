from django.contrib import admin
from cineFast.Models.Filme import Filme
from cineFast.Models.Ator import Ator
from cineFast.Models.Diretor import Diretor
from cineFast.Models.Elenco import Elenco
from cineFast.Models.Comentario import Comentario




# Register your models here.
admin.site.register(Filme)
admin.site.register(Ator)
admin.site.register(Diretor)
admin.site.register(Elenco)
admin.site.register(Comentario)
