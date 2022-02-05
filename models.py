from django.db import models
from django.utils import timezone
# Create your models here.

class Jogos(models.Model):
    class Meta:
        db_table = 'jogos'
        
    nome_jogo = models.CharField(max_length=255)
    data_lancamento = models.DateTimeField(default=timezone.now) 
    console = models.CharField(max_length=300)
    preco = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome_jogo