from django.db import models
from django.utils.html import format_html
from .choices import sexos

# Create your models here.


class Docente(models.Model):
    
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=sexos, default='F', blank=True, null=True) # HAY QUE CREAR EL ARCHIVO CHOICES

    def nombre_completo(self):
        return "{}".format(self.nombres)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'
        


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    credits = models.PositiveSmallIntegerField()
    docente = models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} ({1}) {2}"
        return texto.format(self.nombre, self.credits, self.docente)

    def coloreado(self):
        if self.credits >= 50:
            return format_html('<span style="color:blue;">{0}</span>'.format(self.nombre))
        else:
            return format_html('<span style="color:red;">{0}</span>'.format(self.nombre))
