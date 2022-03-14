from django.contrib import admin
from .models import RolUsuario, Cliente, Proyecto, Tarea

# Register your models here.
admin.site.register(RolUsuario)
admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Tarea)