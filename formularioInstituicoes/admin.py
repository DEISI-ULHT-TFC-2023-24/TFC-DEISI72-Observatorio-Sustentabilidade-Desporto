from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Tipo_Informacao_Principal)
admin.site.register(Tipo_Informacao_Especifica)
