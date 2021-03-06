import math

print("_"*65, "Zadanie 1")
"""Zadanie 3.1 Funkcje liczbowe
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i
zwraca przeliczoną wartość"""

"""1. stopy_na_metry  - przelicza odległość wyrażoną w stopach na metry,"""
def przelicz(stopa:float):
    dlugosc_a = round(stopa/3.28084,3)
    print(f'{stopa} ft. to {dlugosc_a} metra')
przelicz(5.3)

"""2. max  - zwraca większą z dwóch liczb - postaraj się nie używać funkcji max
wbudowanej w pythona"""
def wartosci(liczba1: float,liczba2: float):
    if liczba1 > liczba2:
        print(f'Pierwsza z podanych liczb czyli liczba {liczba1} jest większa')
    else:
        print(f'Druga z podanych liczb czyli liczba {liczba2} jest większa')
wartosci(7,6)

"""3. srednia  - oblicza średnią z dwóch liczb"""
def wartosci2(liczba1: float,liczba2: float):
    wynik = (liczba1 + liczba2)/2
    print(f'Średnia podanych liczb to: {wynik}')

wartosci2(4,6)

"""4. pole_kola  - oblicza pole koła o podanym promieniu (jeden parametr) podpowiedź:
wartość PI jest dostępna jako Math.PI"""

def pole_kola(promien: float):
    pole = round(math.pi * promien**2,2)
    print(f'Pole koła o promieniu {promien} wynosi: {pole} cm2')
pole_kola(30)


"""5. bmi  - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w
metrach i wagi w kg."""

def oblicz_bmi(wzrost: float, waga: float):
    """

    :param wzrost: Podajemy wzrost w metrach np 1.72
    :param waga: Podajemy wagę w kilogramach
    :return: Otrzymujemy nasz współczynnik BMI wraz z opisem czy jest właściwy
    """
    bmi = round((waga / (wzrost)**2),2)
    if bmi <16:
        print(f'BMI: {bmi} Wygłodzenie (niedowaga)')
    if bmi >= 16 and bmi < 17:
         print(f'BMI: {bmi} Wychudzenie (niedowaga)')
    if bmi >= 17 and bmi < 18.5:
        print(f'BMI: {bmi} Niedowaga')
    if bmi >= 18.5 and bmi < 25:
         print(f'BMI: {bmi} Pożądana masa ciała (optimum)')
    if bmi >= 25 and bmi < 30:
         print(f'BMI: {bmi} Nadwaga (nadwaga)')
    if bmi >= 30 and bmi < 35:
         print(f'BMI: {bmi} Otyłość 1 stopnia (otyłość)')
    if bmi >= 35 and bmi < 40:
         print(f'BMI: {bmi} Otyłość 2 stopnia  (duża otyłość)')
    if bmi >= 40:
         print(f'BMI: {bmi} Otyłość 3 stopnia (chorobliwa otyłość)')

oblicz_bmi(1.72,72)


"""
6. pole_trojkata  - z trzema parametrami - oblicza pole trójkąta o podanych bokach
z wzoru Herona."""

# skorzytałem z zadania domowgo  robionego przeze mnie na poprzednim zjezdzie. Dostosowałem je jedynie do funkcji

import math

def pole_trojkonta(ab: int, bc: int, ac: int):
    Polowa_obwodu = (ab+bc+ac)/2
    pole = math.sqrt(Polowa_obwodu * (Polowa_obwodu - ab) * (Polowa_obwodu - bc) * (Polowa_obwodu - ac))
    if ab < (bc + ac) and bc < (ab + ac) and ac < (ab + bc) :
        print("Z tych odcinków można zbudować trójkąt")
    else:
        print("Z tych odcinków nie da się zbudować trójkąta")
    print(f'Pole trójkonta wynosi: {round(pole,2)} cm2')
pole_trojkonta(4,5,6)

"""
7. kilometry_na_mile  - przelicza odległość wyrażoną w kilometrach na mile"""

def kilometry_na_mile(kilometry: float):
    odleglosc = round(kilometry*0.621,5)
    print(f'Podana odległość w kilometrach odpowiada odległości w milach, równej: {odleglosc} mili')

kilometry_na_mile(1)


"""8. mile_na_kilometry  - przelicza odległość wyrażoną w milach na kilometry"""
def mile_na_kilometry(mile: float):
    odleglosc = round(mile/0.621,3)
    print(f'Podana odległość w milach odpowiada odległości w kilometrach, równej: {odleglosc} km')

mile_na_kilometry(1)

print("_"*65, "Zadanie 2")

"""Zadanie 3.2 | MiesiąceZapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
Logikę obliczania liczby dni wydziel do osobnej funkcji.
Wersja A Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
Wersja B (trudniejsza) Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie 
policz czy w tym roku luty był przestępny czy nie.
"""

# nazwa_miesiaca = input("podaj nazwę miesiąca:")
# if nazwa_miesiaca == "Luty":
#     rok = int(input("Podaj rok, który cię interesuje"))
#     if rok %4 == 0:
#         if rok%100 == 0 and rok %400 != 0:
#             print(f'{nazwa_miesiaca} ma 28 dni')
#         else:
#             print(f'{nazwa_miesiaca} ma 29 dni')
#     else:
#         print(f'{nazwa_miesiaca} ma 28 dni')
# elif nazwa_miesiaca == "Styczeń" or nazwa_miesiaca == "Marzec" or nazwa_miesiaca == "Maj" or nazwa_miesiaca == "Liepiec" or nazwa_miesiaca == "Sierpień" or nazwa_miesiaca == "Październik" or nazwa_miesiaca == "Grudzień":
#     print(f'{nazwa_miesiaca} ma 31 dni')
# elif nazwa_miesiaca == "Kwiecień" or nazwa_miesiaca == "Czerwiec" or nazwa_miesiaca == "Wrzesień" or nazwa_miesiaca == "Listopad":
#     print(f'{nazwa_miesiaca} ma 30 dni')



print("_"*65, "Zadanie 3")
"""Zadanie 3.3 | Operacje na listach
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie
wykona odpowiednie operacje i zwróci odpowiedni wynik
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)"""


"""1 suma"""

def suma(liczba1: float, liczba2: float, liczba3: float, liczba4:float):
    wynik = liczba1 + liczba2 + liczba3 + liczba4
    print(f'Suma podanych liczb to: {wynik}')
suma(1,2,3,4.7)


"""2. Średnia"""
def srednia(liczba1: float, liczba2: float, liczba3: float, liczba4:float):
    wynik = (liczba1 + liczba2 + liczba3+ liczba4)/4
    print(f'Średnia podanych liczb to: {wynik}')
srednia(1,2,3,4)

"""3.max"""
lista = [10,20,30,40]
for a in lista:
   for b in lista:
    wynik = a-b
    print(wynik)







print("_"*65, "Zadanie 4")
"""
Zadanie 3.4 | Zliczanie znaków
Napisz funkcję zliczającą liczbę znaków w podanym przez użytkownika napisie pomiędzy
zadanymi przez użytkownika znakami (np. <>).
Nawiasy mogą wystąpić tylko raz.
Przykład użycia:
policz_znaki('ala ma <kota> a kot ma ale')
4
policz_znaki('ala ma kota a (kot) ma ale', '(', ')')
3
"""

# tekst = input('Podaj dowlony tekst. Zliczona zostanie ilość znaków pomiędzy <>')
# wynik = tekst.index('>') - tekst.index('<')-1
# print(f'Długość tekstu wynosi:{len(tekst)}. Ilość znaków w nawiasie "<>" to: {wynik} (Spacje są uzględniane)')
#
# print("_"*65, "Zadanie 5")


zakres= [10,20,30,40]
ilosc = 0
for a in zakres:
    for b in zakres:
        if a > b:
            ilosc =+1
print(ilosc)




