from django.db import models

# Create your models here.


class SensorData(models.Model):
    id = models.AutoField(primary_key=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'sensordata'  # Nombre de la tabla en la base de datos
        managed = False           # Indica a Django que la tabla ya existe

    def __str__(self):
        return f"{self.datetime}: {self.temperature}°C, {self.humidity}%"
