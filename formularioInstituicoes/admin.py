from django.contrib import admin

# Register your models here.

from .models import *

class TemaAdmin(admin.ModelAdmin):
    pass # filter_horizontal = ('subtemas',)

admin.site.register(Tema, TemaAdmin)

class SubTemaAdmin(admin.ModelAdmin):
    pass # filter_horizontal = ('perguntas',)
    list_display = ('nome', 'tema')
    ordering=('tema', 'nome')

admin.site.register(SubTema, SubTemaAdmin)
admin.site.register(Instalacao)
admin.site.register(Pergunta)
admin.site.register(Resposta)

class QuestionarioAdmin(admin.ModelAdmin):
    pass # filter_horizontal = ('temas',)

admin.site.register(Questionario, QuestionarioAdmin)
admin.site.register(Avaliacao)
admin.site.register(Entidade)

