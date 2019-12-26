import datetime
from django.db import models
from django.utils import timezone

class Empleado(models.Model):
    idEmpleado= models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    password=models.CharField(max_length=20)
    edad=models.IntegerField()
    sueldo=models.FloatField()
    fechaNacimiento=models.DateField()
    idDepartamento=models.CharField(max_length=20)
    responsable=models.BooleanField()

    def __str__(self):
        return str(self.idEmpleado)


"  question = models.ForeignKey(Question, on_delete=models.CASCADE)"
class Departamento(models.Model):
    codDepartamento=models.IntegerField(primary_key=True)
    tipo=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=100)

    def __str__(self):
        return self.codDepartamento


class Especialidad(models.Model):
    idEspecialidad=models.IntegerField(primary_key=True)
    tipo=models.CharField(max_length=100)
    empleado=models.CharField(max_length=10)

    def __str__(self):
        return self.idEspecialidad

class Servicio(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    nombre=models.CharField(max_length=20)
    valorHora=models.FloatField()

class Cliente(models.Model):
    ruc_cedula=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=60)
    responsable=models.CharField(max_length=60)
    direccion=models.CharField(max_length=100)

class Reporte(models.Model):
    nroReporte=models.IntegerField(primary_key=True)
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha=models.DateField()
    ordenTrabajo=models.CharField(max_length=50)
    horaInicio=models.DateField()
    horaFinal=models.DateField()
    solucionado=models.BooleanField()
    contrato=models.BooleanField()
    facturar=models.BooleanField()
    solicitadoPor=models.CharField(max_length=50)
    observaciones=models.CharField(max_length=200)

class ReporteDetalle(models.Model):
    idDetalleR=models.IntegerField(primary_key=True)
    nroReporte=models.ForeignKey(Reporte, on_delete=models.CASCADE)
    rubro=models.IntegerField()
    descripcion=models.CharField(max_length=200)
    tiempoTotal=models.TimeField()

class Producto(models.Model):
    idProducto=models.IntegerField(primary_key=True)
    marca=models.CharField(max_length=14)
    valorCompra=models.FloatField()
    valorVenta=models.FloatField()
    stock=models.IntegerField()
    descripcion=models.CharField(max_length=200)

class CompraProducto(models.Model):
    idCompra=models.IntegerField(primary_key=True)
    idCliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idProducto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    valorTotal=models.FloatField()

class Contato(models.Model):
    idContato=models.IntegerField(primary_key=True)
    idCliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado=models.BooleanField()
    fechaContrato=models.DateField()
    imagenContrato=models.CharField(max_length=50)
    contratoTacito=models.BooleanField()
    descripcion=models.CharField(max_length=200)
