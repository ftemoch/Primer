from django.db import models

# Create your models here.
class Cliente(models.Model):
  TIPO_CLIENTE = (
    ('Gobierno', 'Gobierno'),
    ('Particular', 'Particular'),
    ('Empresarial', 'Empresarial'),
  )
  NIT = models.CharField(max_length=40, null=True)
  nombre = models.CharField(max_length=100, null=True)
  direccion = models.CharField(max_length=200, null=True)
  telefono = models.CharField(max_length=40, null=True)
  email = models.CharField(max_length=100, null=True)
  tipo_cliente = models.CharField(max_length=40, null=True, choices=TIPO_CLIENTE)
  fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
		  return self.nombre


class Equipo(models.Model):
  TIPO_EQUIPO = (
    ('Impresora', 'Impresora'),
    ('Escritorio', 'Escritorio'),
    ('Portatil', 'Portatil'),
    ('Escaner', 'Escaner'),
  )
  CONDICION_EQUIPO = (
    ('Dañado', 'Dañado'),
    ('Utilizable', 'Utilizable'),
    ('Reparado', 'Reparado'),
    ('EsperaRepuesto', 'EsperaRepuesto'),
  )
  nombre = models.CharField(max_length=120, null=True)
  tipo_equipo = models.CharField(max_length=40, null=True, choices=TIPO_EQUIPO)
  serial = models.CharField(max_length=40, null=True)
  marca = models.CharField(max_length=40, null=True)
  proveedor = models.CharField(max_length=40, null=True)
  caracteristicas = models.CharField(max_length=400, null=True)
  condicion_equipo = models.CharField(max_length=40, null=True, choices=CONDICION_EQUIPO)
  anotaciones = models.CharField(max_length=100, null=True)
  fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
  costo_reposicion = models.FloatField(null=True)

  def __str__(self):
    return self.nombre


class Contrato(models.Model):
  ESTADO_CONTRATO = (
    ('En ejecucion', 'En ejecucion'),
    ('Terminado', 'Terminado'),
    ('Pendiente', 'Pendiente'),
    ('Cancelado', 'Cancelado'),
  )
  TECNICO = (
    ('Ricardo Aleman', 'Ricardo Aleman'),
    ('Hernan Vidaure', 'Hernan Vidaure'),
    ('Jeyson Porras', 'Jeyson Porras'),
    ('Natalia Ramirez', 'Natalia Ramirez'),
  )
  cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
  equipo = models.ForeignKey(Equipo, null=True, on_delete=models.SET_NULL)
  nroContrato = models.CharField(max_length=30, null=True)
  fecha_inicio = models.DateTimeField(auto_now_add=True, null=True)
  fecha_terminacion = models.DateTimeField(auto_now_add=True, null=True)
  print = models.CharField(max_length=100, null=True)
  fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
  valor = models.FloatField(null=True)
  estado_contrato = models.CharField(max_length=60, null=True, choices=ESTADO_CONTRATO)
  tecnico = models.CharField(max_length=60, null=True, choices=TECNICO)

  def __str__(self):
    return self.nroContrato