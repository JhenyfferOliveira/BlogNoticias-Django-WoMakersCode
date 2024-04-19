from django.shortcuts import render
from comentarios.forms import ComentForm
from comentarios.models import Comentario

# Create your views here.
def criar_coment(request):
    sucesso = False
    form = ComentForm(request.POST or None)

    if form.is_valid():
        form.save()
        sucesso = True

    contexto = {
        'form': form,
        'sucesso': sucesso,
    }

    return render(request, 'criar_coment.html', contexto)