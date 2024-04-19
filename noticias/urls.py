from django.urls import path
from noticias.views import criar_noticia, painel_noticias, aprovar_noticia, reprovar_noticia, visualizar_noticia

app_name = 'Noticias'
urlpatterns = [
    path('criar_noticia/', criar_noticia, name='criar_noticia'),
    path('painel_noticias/', painel_noticias, name='painel_noticias'),
    path('aprovar_noticia/<int:id_noticia>/', aprovar_noticia, name='aprovar_noticia'),
    path('reprovar_noticia/<int:id_noticia>/', reprovar_noticia, name='reprovar_noticia'),
]