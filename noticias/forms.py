from django import forms
from noticias.models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'data', 'categoria', 'conteudo',  'destaque', 'imagem']