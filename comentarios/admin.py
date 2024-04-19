from django.contrib import admin
from comentarios.models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'noticia', 'data']
    search_fields = ['nome', 'noticia']
    list_filter = ['data']
    