from django.db import models

# Create your models here.
class User(models.Model):
    roles = (
        ('Master', 'Master'),
        ('Autor', 'Autor'),
        ('Editor', 'Editor'),
    )
    
    nome = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    senha = models.CharField(max_length=50)
    role = models.CharField(max_length=8, choices=roles)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    