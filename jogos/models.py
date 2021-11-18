from django.db import models

class Jogos(models.Model):
    nome_jogo = models.CharField(max_length=50)
    """ imagem_capa = models.ImageField() """
    data_lancamento = models.DateField()
    sinopse = models.TextField()
    
    def __str__(self):
        return self.nome_jogo
