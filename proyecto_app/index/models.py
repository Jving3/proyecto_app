from django.db import models

# Create your models here.
class Personal (models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    cargo = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(upload_to='personal', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='profesional'
        verbose_name_plural = 'profesionales'
    
    def __str__(self):
        return self.nombre