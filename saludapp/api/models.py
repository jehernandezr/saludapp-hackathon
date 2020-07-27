from django.db import models



class User(models.Model):
    #relaciones

    #atributos
    cedula = models.AutoField(primary_key=True)
    fechaNacimiento = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return '%s, %s, %s' % (self.cedula.__str__(), self.apellido.__str__(), self.nombre)



class Medico(models.Model):
    #relaciones
    cedula = models.AutoField(primary_key=True)
    fechaNacimiento = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return '%s, %s, %s' % (self.cedula.__str__(), self.apellido.__str__(), self.nombre)


class Cita(models.Model):
    # relaciones
    medico= models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    # atributos
    url=models.URLField(max_length=250,blank=True)
    fechaCita = models.DateTimeField(auto_now_add=False)
    fechaCreada = models.DateField(auto_now_add=True)
    tipoCita = models.CharField(max_length=50)

    def __str__(self):
        return '%s, %s, %s' % (self.tipoCita, self.fechaCita.__str__(), self.paciente)
