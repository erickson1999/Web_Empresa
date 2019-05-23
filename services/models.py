from django.db import models

# Create your models here.

class Project(models.Model):
    descripcion=models.CharField(max_length=50)
    titulo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='proyectos')
    contenido=models.TextField()
    create=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    update=models.DateTimeField(auto_now_add=True,verbose_name='Ultima actualización')

    def __str__(self):
        return self.titulo

