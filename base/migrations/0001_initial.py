# Generated by Django 5.0.3 on 2024-04-05 13:33

from django.db import migrations
from django.core.management import call_command

def populate_db(apps, schema_editor):
    call_command('loaddata', 'usuarios-base.json')

class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]