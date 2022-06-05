from django.shortcuts import render
from django.http import HttpResponse
from biblioteka.models import Autor,Ksiazka

# Create your views here.

def wyswietl(request):
    widok = Autor.objects.all()
    return render(request, "lista_autorow.html", context={"widok": widok})

def pokaz(request):

    autor = Autior.objects.get(id=id)

    return render(request, "szczegoly_autora.html", context={"autor": autor})
