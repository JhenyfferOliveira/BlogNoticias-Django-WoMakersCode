"""
URL configuration for projeto_noticias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from base.views import inicio, noticia_por_categoria, pesquisar_noticias_por_categoria, pesquisar_noticias, pesquisa_nao_encontrada, quem_somos, sobre
from noticias.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('pesquisar/', pesquisar_noticias, name='pesquisar_noticias'),
    path('pesquisa_nao_encontrada/', pesquisa_nao_encontrada, name="pesquisa_nao_encontrada"),
    path('pesquisar/<str:categoria>/', pesquisar_noticias_por_categoria, name='pesquisar_noticias_por_categoria'),
    path('comentarios/', include('comentarios.urls', namespace='comentarios')),
    path('usuario/', include('usuario.urls', namespace='usuario')),
    path('noticias/', include('noticias.urls', namespace='noticias')),

    path('noticia/categoria/<str:categoria>/', noticia_por_categoria, name='noticia_por_categoria'),
    path('noticia/id/<int:id_noticia>/', visualizar_noticia, name='visualizar_noticia'),

    path('tecnologia/', noticia_por_categoria, {'categoria': 'tecnologia'}, name='tecnologia'),
    path('politica/', noticia_por_categoria, {'categoria': 'politica'}, name='politica'),
    path('economia/', noticia_por_categoria, {'categoria': 'economia'}, name='economia'),
    path('esportes/', noticia_por_categoria, {'categoria': 'esportes'}, name='esportes'),
    path('cultura/', noticia_por_categoria, {'categoria': 'cultura'}, name='cultura'),

    path('quem_somos/', quem_somos, name='quem_somos'),
    path('sobre/', sobre, name='sobre')
]
