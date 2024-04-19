from django.shortcuts import render, redirect
from noticias.models import Noticia

def inicio(request):
    noticias_urgentes = Noticia.objects.filter(destaque=True, status='Aprovado')
    ultimas_noticias = Noticia.objects.filter(destaque=False, status='Aprovado').order_by('-data')
    return render(request, 'index.html', {'noticias_urgentes': noticias_urgentes, 'ultimas_noticias': ultimas_noticias})

def pesquisar_noticias(request):
    pesquisa_formulario = request.POST.get('search_query')
    if pesquisa_formulario:
        noticias = Noticia.objects.filter(conteudo__icontains=pesquisa_formulario, status='Aprovado').order_by('-data')
        if noticias.exists():
            return render(request, 'pesquisar_noticias.html', {'noticias': noticias, 'pesquisa_formulario': pesquisa_formulario})
    return pesquisa_nao_encontrada(request)

def pesquisa_nao_encontrada(request):
    return render(request, 'pesquisa_nao_encontrada.html')

def noticia(request):
    return render(request, 'criar_noticia.html', {})

def pesquisar_noticias_por_categoria(request, categoria):
    # Pesquisar notícias com base na categoria
    noticias = Noticia.objects.filter(categoria=categoria, status='Aprovado').order_by('-data')
    return render(request, 'pesquisar_noticias.html', {'noticias': noticias})

def noticia_por_categoria(request, categoria=None):
    noticias = Noticia.objects.filter(status='Aprovado').order_by('-data')  # Retorna todas as notícias por padrão
    
    if categoria:
        noticias = noticias.filter(categoria=categoria)

    categorias = {
        'tecnologia': {'imagem': '/static/images/tecnologia.jpg', 'nome': 'Tecnologia'},
        'economia': {'imagem': '/static/images/economia.jpg', 'nome': 'Economia'},
        'cultura': {'imagem': '/static/images/cultura.jpg', 'nome': 'Cultura'},
        'politica': {'imagem': '/static/images/politica.jpg', 'nome': 'Política'},
        'esportes': {'imagem': '/static/images/esportes.jpg', 'nome': 'Esportes'}
    }

    return render(request, 'noticia_por_categoria.html', {'noticias': noticias, 'categoria': categoria, 'categoria_info': categorias.get(categoria)})

def noticia_por_id(request, id):
    # Busca a notícia pelo ID no banco de dados
    noticia = Noticia.objects.get(pk=id)
    return render(request, 'noticia_por_id.html', {'noticia': noticia})

def comentario(request):
    return render(request, 'comentario.html')

def tecnologia(request):
    return render(request, 'tecnologia.html')

def politica(request):
    return render(request, 'politica.html')

def economia(request):
    return render(request, 'economia.html')

def esportes(request):
    return render(request, 'esportes.html')

def cultura(request):
    return render(request, 'cultura.html') 

def quem_somos(request):
    return render(request, 'quem_somos.html')

def sobre(request):
    return render(request, 'sobre.html')

def login(request):
    return render(request, 'login.html')

def criar_usuario(request):
    return render(request, 'criar_usuario.html')