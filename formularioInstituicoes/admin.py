from django.contrib import admin
from django.contrib.admin import widgets

# Register your models here.

from .models import *
from django import forms


class TemaAdmin(admin.ModelAdmin):
    pass  # filter_horizontal = ('subtemas',)


admin.site.register(Tema, TemaAdmin)


class SubTemaAdmin(admin.ModelAdmin):
    # filter_horizontal = ('perguntas',)
    list_display = ('nome', 'tema')
    ordering = ('tema', 'nome')


admin.site.register(SubTema, SubTemaAdmin)


class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'entidade')


admin.site.register(Instalacao, InstalacaoAdmin)
admin.site.register(Pergunta)


class OpcaoAdmin(admin.ModelAdmin):  # filtar no admin a pergunta que se pretende com dropdown=True
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "pergunta":
            kwargs["queryset"] = Pergunta.objects.filter(tipo='ESCOLHA_MULTIPLA')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('opcao', 'pergunta')


admin.site.register(Opcao, OpcaoAdmin)
admin.site.register(RespostaNumerica)
admin.site.register(RespostaTextual)


class QuestionarioAdmin(admin.ModelAdmin):
    pass  # filter_horizontal = ('temas',)


admin.site.register(Questionario, QuestionarioAdmin)
admin.site.register(Avaliacao)
admin.site.register(Entidade)
