from django.contrib import admin
from usuario.models import User

# Register your models here.
@admin.register(User)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'role', 'data'] 
    search_fields = ['nome','email']
    list_filter = ['role', 'data']