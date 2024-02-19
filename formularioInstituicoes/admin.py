from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Tema)
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(Questionario)
admin.site.register(Avaliacao)
admin.site.register(Entidade)

