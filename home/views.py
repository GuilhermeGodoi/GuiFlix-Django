from django.shortcuts import render, get_object_or_404  
from home.models import Filme
from django.contrib.auth.decorators import login_required


def index(request):
    filmes = Filme.objects.all()
    return render(request, 'index.html', {"cards": filmes})


def about(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    return render(request, 'about.html', {"filme": filme})