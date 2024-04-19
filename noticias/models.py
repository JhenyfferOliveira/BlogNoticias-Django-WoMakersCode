from django.db import models
from django.conf import settings

# Create your models here.
class Noticia(models.Model):
    categorias = (
        ('Esporte', 'Esporte'),
        ('Cultura', 'Cultura'),
        ('Economia', 'Economia'),
        ('Politica', 'Politica'),
        ('Tecnologia', 'Tecnologia'),
    )

    status_noticia = (
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
    )

    titulo = models.CharField(max_length=200)
    data = models.DateField(help_text='dd/mm/aaaa')
    categoria = models.CharField(max_length=50, choices=categorias)
    conteudo = models.TextField()
    destaque = models.BooleanField()
    imagem = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=status_noticia, default=status_noticia[0][0])


def __str__(self):
    return f'{self.titulo}: {self.data}'

class Meta:
    verbose_name = 'Cadastro de Notícia'
    verbose_name_plural = 'Cadastro de Notícias'
    ordering = ['-data']