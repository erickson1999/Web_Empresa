from django.db import models

# Create your models here.

class Project(models.Model):
    titulo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='proyectos')
    contenido=models.TextField()
    create=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creacion')
    update=models.DateTimeField(auto_now=True,verbose_name='Ultima Actualizacion')

    def __str__(self):
        return self.titulo
