from django.db import models

# Create your models here.
class Movie(models.Model):
    nombre = models.CharField(max_length=255)
    año = models.IntegerField()
    actores_principales = models.CharField(max_length=255)
    resumen = models.TextField()
    imagen_url = models.URLField()

    def __str__(self):
        return self.nombre