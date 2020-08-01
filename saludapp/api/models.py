from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.db import models
import datetime



class Paciente(models.Model):
    #relaciones
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    #atributos
    cedula = models.CharField(primary_key=True,max_length=11)
    fechaNacimiento = models.DateField(auto_now_add=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)


    def __str__(self):
        return '%s, %s, %s' % (self.cedula.__str__(), self.apellido.__str__(), self.nombre)



class Medico(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    cedula = models.CharField(primary_key=True,max_length=11)
    fechaNacimiento = models.DateField(auto_now_add=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    phone =models.CharField(max_length=10)

    def __str__(self):
        return '%s, %s, %s' % (self.cedula.__str__(), self.apellido.__str__(), self.nombre)

class Disponible(models.Model):
    #relaciones
    medico= models.ForeignKey(Medico, on_delete=models.CASCADE)
    #atributos
    fecha = models.DateTimeField(auto_now_add=False)
    tipo = models.CharField(max_length=50)
    estado =models.CharField(max_length=250,choices =[('C','Cancelada'),('R','Reservada'),('L','Libre'),('F','Finalizada')],default='L')
    def __str__(self):
        return f'{self.fecha},{self.tipo},{self.estado},{self.medico}'

class Cita(models.Model):
    # relaciones
    medico= models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    disponible = models.ForeignKey(Disponible, on_delete=models.CASCADE,default=None)
    # atributos
    url=models.URLField(max_length=250,blank=True)
    fechaCreada = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s, %s, %s' % (self.fechaCreada.__str__(), self.url.__str__(), self.paciente)
