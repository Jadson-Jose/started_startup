from django.contrib import admin
from .models import Empresas, Documento, Mertricas

# Register your models here.
admin.site.register(Empresas)
admin.site.register(Documento)
admin.site.register(Mertricas)
