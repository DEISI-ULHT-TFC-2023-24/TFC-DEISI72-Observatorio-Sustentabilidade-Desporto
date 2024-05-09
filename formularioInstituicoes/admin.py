from django.contrib import admin
from django.contrib.admin import widgets

# Register your models here.

from .models import *
from django import forms


class TemaAdmin(admin.ModelAdmin):
    pass  # filter_horizontal = ('subtemas',)


admin.site.register(Tema, TemaAdmin)


class SubTemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tema')
    ordering = ('tema', 'nome',)


admin.site.register(SubTema, SubTemaAdmin)


class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'entidade')


admin.site.register(Instalacao, InstalacaoAdmin)


class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('texto','id', 'subtema')


admin.site.register(Pergunta, PerguntaAdmin)

admin.site.register(UnidadePergunta)


class OpcaoAdmin(admin.ModelAdmin):  # filtar no admin a pergunta que se pretende com dropdown=True
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "pergunta":
            kwargs["queryset"] = Pergunta.objects.filter(tipo__in=['ESCOLHA_MULTIPLA_UNICA', 'ESCOLHA_MULTIPLA_VARIAS'])
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    filter_horizontal = ('pergunta',)


admin.site.register(Opcao, OpcaoAdmin)


class RespostaNumericaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'pergunta', 'avaliacao')


admin.site.register(RespostaNumerica, RespostaNumericaAdmin)


class RespostaTextualAdmin(admin.ModelAdmin):
    list_display = ('texto', 'pergunta')


admin.site.register(RespostaTextual, RespostaTextualAdmin)


class QuestionarioAdmin(admin.ModelAdmin):
    filter_horizontal = ('temas',)


admin.site.register(Questionario, QuestionarioAdmin)
admin.site.register(Avaliacao)
admin.site.register(Entidade)
admin.site.register(Ficheiro)

