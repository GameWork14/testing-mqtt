from django.db import models

# Create your models here.
class ventasmqtt(models.Model):
    cliente =   models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    cemento = models.CharField(max_length=255)
    arena = models.CharField(max_length=255)
    grava = models.CharField(max_length=255)
    aditivo = models.CharField(max_length=255)
    placa = models.CharField(max_length=255, default='valor_predeterminado')

    def __str__(self):
        return self.cliente
    
class Alarmasmqtt(models.Model):
    Alarma = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Alarma

class sensor1mqtt(models.Model):
    sensor = models.CharField(max_length=255)
