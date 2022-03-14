from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RolUsuario(models.Model):
    ADMIN = 'ADMIN'
    EMPLEADO = 'EMPLEADO'
    CLIENTE = 'CLIENTE'

    OPCIONES_ROL = (
        (ADMIN, 'Administrador'),
        (EMPLEADO, 'Empleado'),
        (CLIENTE, 'Cliente')
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rol')
    rol = models.CharField(max_length=10,choices=OPCIONES_ROL)

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info_cliente')
    direccion = models.CharField(max_length=250, blank=True)
    asistencia = models.CharField(max_length=250, blank=True)
    informacionAdicional = models.CharField(max_length=500, blank=True)

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    avance = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    fechaInicio = models.DateField()
    fechaLimite = models.DateField()
    direccion = models.CharField(max_length=250, blank=True)
    ubicacion = models.CharField(max_length=100, blank=True)
    informacionAdicional = models.CharField(max_length=500, blank=True)
    usuarioEncargado = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='proyectos_a_cargo')
    usuarioCliente = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='proyectos_cliente') 
    empleadosProyecto = models.ManyToManyField(User)

class Tarea(models.Model):
    # Estados
    SIN_COMENZAR = 'SIN_COMENZAR'
    TRABAJANDO = 'TRABAJANDO'
    TRABADO = 'TRABADO'
    EN_REVISION = 'EN_REVISION'
    TERMINADO = 'TERMINADO'

    OPCIONES_ESTADO = (
        (SIN_COMENZAR, 'Sin comenzar'),
        (TRABAJANDO, 'Trabajando en ello'),
        (TRABADO, 'Trabado'),
        (EN_REVISION, 'En revisión'),
        (TERMINADO, 'Terminado'),
    )

    # Prioridades
    ALTA = 'Alta'
    MEDIA = 'Media'
    BAJA = 'Baja'

    OPCIONES_PRIORIDAD = (
        (ALTA, 'Alta'),
        (MEDIA, 'Media'),
        (BAJA, 'Baja')
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    prioridad = models.CharField(max_length=5, choices=OPCIONES_PRIORIDAD, default=BAJA)
    estado = models.CharField(max_length=25, choices=OPCIONES_ESTADO, default=SIN_COMENZAR)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuarioEmpleado = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='tareas_a_cargo')