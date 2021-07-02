from django.db import models
from django.db.models.expressions import OrderBy

# Create your models here.


class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ['title']

    def __str__(self):
        return self.title
