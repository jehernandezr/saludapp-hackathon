from django.db import models


class RegistroVenta(models.Model):
    #relaciones
    fiado = models.OneToOneField('usuarios.Fiado', on_delete=models.CASCADE, null=True, blank=True)
    tienda = models.ForeignKey('inventarios.Tienda', on_delete=models.CASCADE)
    #atributos
    valorVenta = models.FloatField(null=True, blank=True, default=None)
    fechaVenta = models.DateField(auto_now_add=True)
    metodoPago = models.CharField(max_length=50)

    def __str__(self):
        return '%f, %s, %s' % (self.valorVenta, self.fechaVenta.__str__(), self.metodoPago)

class Pedido(models.Model):
    #relaciones
    tienda = models.ForeignKey('inventarios.Tienda', on_delete=models.CASCADE)
    #atributos
    nPedido = models.AutoField(primary_key=True)
    fechaPedido = models.DateField(auto_now_add=True)
    refSeguimiento = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.nPedido.__str__(), self.fechaPedido.__str__(), self.refSeguimiento, self.estado)