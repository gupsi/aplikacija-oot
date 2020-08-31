from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.
from .models import *

class OSatiAdmin(admin.ModelAdmin):
	list_display = ['datum', 'pvremena', 'kvremena', 'korisnik']

admin.site.register(OdradjeniSati, OSatiAdmin)
admin.site.register(ListaZadataka)
admin.site.register(Profile)
