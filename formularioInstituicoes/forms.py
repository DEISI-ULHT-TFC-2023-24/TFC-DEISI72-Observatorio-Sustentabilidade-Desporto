from django.forms import ModelForm
from django import forms
from .models import *


class FormNumerosInteiros(ModelForm):
    class Meta:
        model = RespostaNumerica
        fields = ('texto',)


# class FormTextoLivre(ModelForm):
# class FormEscolhaMultipla(ModelForm):
