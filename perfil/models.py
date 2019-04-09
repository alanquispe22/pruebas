from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    alias = models.CharField(verbose_name="Alias", max_length=30)
    nombre = models.CharField(verbose_name="Nombre", max_length=30)
    apellido = models.CharField(verbose_name="Apellido", max_length=30)
    correo = models.EmailField(verbose_name="Correo")
    password = models.

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
