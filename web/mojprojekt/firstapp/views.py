from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Produkt

# Create your views here.
def widok(request):
    return HttpResponse(f'To jest mój pierwszy widok!')

def hello (request, imie):
    return  HttpResponse(f"Witaj, {imie}!")

def dzialanie(request,operacja,liczba1,liczba2):
    if operacja == "mnozenie":
        wynik = float(liczba1) * float(liczba2)
    elif operacja == "dzielenie":
        wynik = float(liczba1) / float(liczba2)
    elif operacja == "dodawanie":
        wynik = float(liczba1) + float(liczba2)
    elif operacja == "odejmowanie":
        wynik = float(liczba1) - float(liczba2)
    elif operacja == "potegowanie":
        wynik = float(liczba1) ** float(liczba2)

    return HttpResponse(f'Wybrane przez Ciebie działanie: {operacja}, na liczbach {liczba1} i {liczba2} dało w wyniku {wynik}')

# def produkty(request):
#     prods = Produkt.objects.filter(dostepnosc=True)
#     lista = []
#     for p in prods:
#         lista.append(f"<li>{p.nazwa} - {p.dostepnosc} <li>")
#     napis = "/n".join(lista)
#     return render(request, "templates.html", context={"produkty": prods})

def produkty(request):
    prods = Produkt.objects.filter(dostepnosc=True)
    lista = []
    for p in prods:
        lista.append(f"<li>{p.nazwa} - {p.dostepnosc} <li>")
    napis = "/n".join(lista)
    return render(request, "templates.html", context={"produkty": prods})

def szczegoly_produktu(request,id):
    prod = Produkt.objects.get(id=id)
    return render(request, "szczegoly_produktu.html", context={"prod": prod})