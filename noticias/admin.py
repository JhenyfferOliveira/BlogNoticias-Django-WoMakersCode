from django.contrib import admin
from noticias.models import Noticia

# Register your models here.
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'status', 'destaque', 'data'] 
    search_fields = ['titulo']
    list_filter = ['categoria', 'status', 'destaque', 'data']