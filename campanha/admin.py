from django.contrib import admin

# Register your models here.
from .models import Usuario, Agenda, Evento, Logistica, MaterialMarketing, Demanda

admin.site.register(Usuario)
admin.site.register(Agenda)
admin.site.register(Evento)
admin.site.register(Logistica)
admin.site.register(MaterialMarketing)
admin.site.register(Demanda)