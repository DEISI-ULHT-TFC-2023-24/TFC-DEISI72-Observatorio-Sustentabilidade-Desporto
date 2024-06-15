import calendar
import datetime
import locale

from django.contrib import messages
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form
from django import forms
from django.http import request
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible, ReCaptchaV3

from .models import *


class FormNumerosInteiros(ModelForm):
    class Meta:
        model = RespostaNumerica
        fields = ['numero']
        labels = {'numero': ''}

        numero = forms.NumberInput(attrs={
            'required': False,
            'min': 0,
        })


class FormTextoLivre(ModelForm):
    class Meta:
        model = RespostaTextual
        fields = ['texto']
        labels = {'texto': ''}

        texto = forms.Textarea(attrs={'required': False})


class FormEscolhaMultiplaUnica(ModelForm):
    opcao = forms.ModelChoiceField(queryset=Opcao.objects.all(), label=False, required=False)

    class Meta:
        model = RespostaTextual
        fields = ['opcao']
        labels = {'opcao': ''}

        opcao = forms.Textarea(attrs={'required': False})


class FormEscolhaMultiplaVarias(ModelForm):
    opcoes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label=False, required=False)

    class Meta:
        model = RespostaTextual
        fields = ['opcoes']


class FormFicheiro(ModelForm):
    class Meta:
        model = Ficheiro
        fields = ['ficheiro']
        labels = {'ficheiro': ''}
        widgets = {
            'ficheiro': forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
        }

        ficheiro = forms.Textarea(attrs={'required': False})


class FormMes(ModelForm):
    month_choices = [
        ('', ''),
        ('Janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro'),
    ]
    month = forms.ChoiceField(choices=month_choices, label='', required=False)

    class Meta:
        model = RespostaTextual
        fields = ['month']
        labels = {'month': ''}


class FormEntidade(ModelForm):
    captcha = ReCaptchaField(label='', required=True)

    captcha.error_messages["captcha_invalid"] = "Erro a verificar o reCAPTCHA, por favor tente novamente"
    captcha.error_messages["captcha_error"] = "Erro a verificar o reCAPTCHA, por favor tente novamente"

    class Meta:
        model = Entidade
        fields = []
        labels = {}

class FormInstalacoes(ModelForm):
    class Meta:
        model = Instalacao
        fields = ['nome', 'morada', 'distrito', 'concelho', 'freguesia', 'telefone', 'email']
        labels = {'nome': "Nome da Instalação"}

    def __init__(self, *args, **kwargs):
        super(FormInstalacoes, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True


class SignupForm(UserCreationForm):
    error_messages = {
        "password_mismatch": "As passwords não correspondem.",
        "duplicate_email": "Este email já está em uso.",
        "duplicate_username": "Já existe uma instalação com este nome."
    }

    class Meta:
        model = User
        fields = ("username", "email")
        labels = {
            'username': 'Nome entidade',
            'email': 'Email',
        }
        help_texts = {
            'username': '',
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        for field in self.fields.values():
            field.help_text = ''
            field.error_messages = {
                'required': '',
                'invalid': '',
            }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                self.error_messages["duplicate_email"],
                code="duplicate_email",
            )
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                self.error_messages["duplicate_username"],
                code="duplicate_username",
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2
