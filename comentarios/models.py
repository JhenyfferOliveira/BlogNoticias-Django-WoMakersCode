from django.db import models 

# Create your models here.
class Comentario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    texto = models.TextField()
    noticia = models.TextField()
    data = models.DateField(help_text='dd/mm/yyyy')
    
    def __str__(self):
        return f'{self.noticia}:{self.texto},{self.nome}'
class Meta:
    verbose_name = 'Cadastro de comentario'
    verbose_name_plural = 'Cadastros de comentarios'
    ordering = ['-data']

   