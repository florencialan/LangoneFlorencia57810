from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Capacitaciones)
admin.site.register(Asesorias)
admin.site.register(Gestiones)
admin.site.register(Soluciones)

