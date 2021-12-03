from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Noticia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    sinopse = models.TextField()
    descricao = models.TextField()
    # imagem = models.ImageField()

    created_on = models.DateField(default=now)
    update_on = models.DateField()


    def __str__(self):
        return self.nome
