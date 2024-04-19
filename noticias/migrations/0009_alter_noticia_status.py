# Generated by Django 4.2.11 on 2024-04-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0008_remove_noticia_sub_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado')], default='Pendente', max_length=50),
        ),
    ]
