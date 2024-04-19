from django.shortcuts import render, redirect
from noticias.forms import NoticiaForm
from noticias.models import Noticia

# Create your views here.
def criar_noticia(request):
    form = NoticiaForm(request.POST or None)
    sucesso = False

    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }
    
    return render(request, 'criar_noticia.html', contexto)

def painel_noticias(request):
    noticias = Noticia.objects.filter(status='Pendente')

    return render(request, 'painel_noticias.html', {'noticias': noticias})

def aprovar_noticia(request, id_noticia):
    noticia = Noticia.objects.get(id=id_noticia)
    noticia.status = 'Aprovado'
    noticia.save()

    return redirect('noticias:painel_noticias')

def reprovar_noticia(request, id_noticia):
    noticia = Noticia.objects.get(id=id_noticia)
    noticia.status = 'Reprovado'
    noticia.save()

    return redirect('noticias:painel_noticias')

def visualizar_noticia(request, id_noticia):
    noticia = Noticia.objects.get(id=id_noticia)

    return render(request, 'noticia_por_id.html', {'noticia': noticia})