from django.db import models

# Create your models here.
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto[:30]