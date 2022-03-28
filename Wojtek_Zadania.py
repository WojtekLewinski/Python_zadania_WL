badanie = int(input("W skali od 1 do 10 jak bardzo poleciłbys szkolenie w ALX"))

if badanie >= 9:
    print("promotorzy")

if badanie >=7 and badanie <9:
    print("neutralni")

if badanie <=6:
    print("detraktorzy")

# komentarz, na to python nie patrzy
# string
print("Hello world!")
print('Hello world!')
print('Ksiazka "Pan Tadeusz"')
print("Ksiazka 'Pan Tadeusz'")
print("Ksiazka \"Pan Tadeusz\"")  # "eskejpowanie"
print("A \\n")
print("Pierwsza linia\nDruga linia")
print("Pierwsza liniaDruga linia")
print("""Pierwsza linia
Druga linia""")
print('''Ala
ma
kota''')

# int
print(15)
print(-10)

# float
print(2.5)
print(10 + 2.0)

# liczby zespolone
print(3 + 5j)

# problemy z liczbami ulamkowymi...
print(0.1 * 3.0)

# bool
print(True)
print(False)

# None
print(None)

print()
print("Piotr")
print("Marek", 13)

print(10 + 15)  # wyrazenie z operatorem +

# operatory arytmetyczne
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # dzielenie calkowitoliczbowe
print(10 ** 3)
print(9 ** 0.5)
print(10 % 3)  # modulo, reszta z dzielenia

print("Ala" + "ma kota")  # laczenie napisow, konkatenacja
# print("Ala" + 10)
print("Ala" + str(10))
print("Ala\n" * 5)
print('-' * 60)

# zmienne
imie = 'Piotr'  # = - operator przypisania, == UWAGA! robi coś innego!!!
print(imie)
print(type(imie))

imie = 44
print(imie)
print(type(imie))

# schemat nazywania zmiennych - PEP8 https://peps.python.org/pep-0008/
imie_i_nazwisko = 'Piotr Grabski-Gradzinski'

imie_i_nazwisko = 44

print('-' * 60)

# wczytywanie danych od uzytkownika
# imie = input('Podaj imie: ')  # input zawsze zwraca str!
# print(imie)
# print(type(imie))

print('-' * 60)

# operatory porownania - daje nam True albo False
print(1 == 1)  # True, a rowne b
print(1.0 == 1)  # True
print("1" == 1)  # False
print(int("1") == 1)  # True
print(1 != 1)  # False, a rozne od b
print(1 > 1)  # False, a wieksze od b
print(1 >= 1)  # True, a wieksza badz rowne b
print(1 < 1)  # False
print(1 <= 1)  # True

print('-' * 60)

# operatory logiczne
print(True and True)  # True, i, koniunkcja
print(True or False)  # True, lub, alternatywa
print(not True)  # False, przeczenie

print('-' * 60)

print(9 % 3)  # reszta z dzielenia: 0
print(10 % 3)  # reszta z dzielenia: 1


print('-' * 60)


# petla while
# wyswietlanie liczb od 1 do ...
print(1)
print(2)
print(3)
print(4)

print('---')

liczba = 1
while liczba <= 100:
    print(liczba)
    liczba = liczba + 1


print('-' * 60)

while True:
    liczba = int(input('Podaj liczbe: '))
    print(liczba)

    if liczba == 10:
        break
liczba = int(input('Podaj liczbe: '))

print('Jestem przed ifem')

if liczba == 10:
    print('Brawo! Wygrales!')
    print('Podales liczbe 10')
elif liczba == 15: # elif = else if
    print('No to teraz podales 15, ale sprobuj jeszcze raz')
elif liczba == 20:
    print('Podales 20')
else:
    print('Zaden z warunkow nie zostal spelniony')

print('Jestem po ifie')


# zad_1.py
"""
Korzystając z przypisywania wartości do zmiennych,
napisz program obliczający pole trapezu
o długości podstaw 3 i 9 oraz wysokości 6.5.
"""

podstawa_a = 3
podstawa_b = 9
wysokosc = 6.5

# kolejnosc wykonywania operatorow: https://docs.python.org/3/reference/expressions.html#operator-precedence
pole_trapezu = 1 / 2 * (podstawa_a + podstawa_b) * wysokosc
print(pole_trapezu)


"""
Napisz program wypisujący na konsolę Twoje imię i wzrost.
Do przechowywania informacji o Twoim imieniu i wzroście użyj
zmiennych.

Przykładowy komunikat programu:
Imię: Jan
Wzrost: 180
"""

imie = 'Jan'
wzrost = 180

print("Imie: " + imie)
print("Wzrost: " + str(wzrost))

print("Imie: " + imie + "\nWzrost: " + str(wzrost))

print("Imie:", imie)
print("Wzrost:", wzrost)


"""
Napisz program wypisujący na konsolę Twoje imię i wzrost.
Do przechowywania informacji o Twoim imieniu i wzroście użyj
zmiennych.
Zapytaj użytkownika o imię i wzrost.

Przykładowy komunikat programu:
Imię: Jan
Wzrost: 180
"""

imie = input('Podaj imie: ')
wzrost = int(input('Podaj wzrost: '))

print("Imie: " + imie)
print("Wzrost: " + str(wzrost))

print("Imie: " + imie + "\nWzrost: " + str(wzrost))

print("Imie:", imie)
print("Wzrost:", wzrost)

"""
Napisz program wyliczający kwotę należną za zakupiony
towar na podstawie ceny za kilogram oraz liczby zakupionych
kilogramów.
Do przechowywania informacji o cenie oraz liczbie kilogramów
użyj zmiennych.
Wypisz wszystkie informacje na konsolę.

Przykładowy komunikat programu:
Podaj cene za kg: 10.0
Podaj wage: 2.5
Należność: 25.0
"""

cena = float(input('Podaj cene za kg: '))
waga = float(input('Podaj wage: '))

naleznosc = round(cena * waga, 2)
print(type(naleznosc))


print('Naleznosc:', naleznosc, 'PLN')  # 3 argumenty przekazane do printa

print('Naleznosc: ' + str(naleznosc) + ' PLN')

naleznosc_napis = 'Naleznosc: ' + str(naleznosc) + ' PLN'
print(naleznosc_napis)  # 1 argument przekazany do printa

# f-string, formatted string, https://docs.python.org/3/library/string.html#format-specification-mini-language
naleznosc = cena * waga
naleznosc_napis = f'Naleznosc: {naleznosc:_^15.2f} PLN'
print(naleznosc_napis)

"""
Napisz program obliczający koszt przejazdu z miasta A do B na
podstawie podanej
przez użytkownika liczby kilometrów, ceny paliwa oraz spalania.
Zapytaj użytkownika także o nazwy miejscowości.

Przykładowe komunikaty programu:
Podaj miasto A: Warszawa
Podaj miasto B: Gdańsk
Podaj dystans Warszawa-Gdańsk: 420
Podaj cene paliwa: 4.55
Spalanie na 100 km: 5.5
Koszt przejazdu Warszawa-Gdańsk to 105.11 PLN

100 km  - spalanie
dystans - x
"""
miasto_a = input('Podaj miasto A: ')
miasto_b = input('Podaj miasto B: ')
dystans = float(input(f'Podaj dystans {miasto_a}-{miasto_b}: '))
cena = float(input('Podaj cene paliwa: '))
spalanie = float(input('Spalanie na 100 km: '))

koszt = dystans * spalanie / 100.0 * cena

print('Koszt przejazdu ', miasto_a, '-', miasto_b, 'to', koszt, 'PLN')  # wiele argumentow w print
print('Koszt przejazdu' + miasto_a + '-' + miasto_b + ' to ' + str(koszt) + ' PLN')  # konkatenacja stringow
print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.2f} PLN')  # f-string

koszt_napis = f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.2f} PLN'
print(koszt_napis)

"""
Napisz program sprawdzający czy podana przez użytkownika liczba:
- (jest nieparzysta, podzielna przez 3 i większa od 10)
- lub jest to liczba 7.
"""

liczba = int(input('Podaj liczbe calkowita: '))

wynik = (liczba % 2 != 0 and liczba % 3 == 0 and liczba > 10) or liczba == 7

print(wynik)

"""
Napisz program, który na podstawie wprowadzonych wymiarów opakowania (x, y, z) obliczy
jego objętość oraz sprawdzi, czy jest ona większa od 1 litra (1000 cm3).
"""

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
z = int(input('Podaj z: '))

objetosc = x * y * z
czy_wieksze_od_litra = objetosc > 1000

print(f'Objetosc: {objetosc}')
print(f'Czy objetosc jest wieksza od 1l: {czy_wieksze_od_litra}')

"""
Napisz program, który zapyta uzytkownika o liczbę całkowitą.
Jeżeli uzytkownik poda liczbę 10, wtedy wyświetl komunikat:
Podałeś szczęśliwy numerek! Wygrałeś!
W przeciwnym wypadku wyświetl:
Spróbuj jeszcze raz!
"""

liczba = int(input('Podaj liczbe calkowita: '))

if liczba == 10:
    print('Podałeś szczęśliwy numerek! Wygrałeś!')
else:
    print('Spróbuj jeszcze raz!')


"""
Napisz program, który sprawdzi pełnoletność osoby na podstawie roku jej urodzenia.

Przykładowy komunikat programu:
Podaj rok urodzenia: 1980
Jesteś pełnoletni!
"""

import datetime

rok_urodzenia = int(input('Podaj rok urodzenia: '))
aktualny_rok = datetime.date.today().year
print(aktualny_rok)
wiek = aktualny_rok - rok_urodzenia

if wiek >= 18:
    print('Jesteś pełnoletni')
else:
    print('NIE jesteś pełnoletni')

"""
Napisz program, który na podstawie dwóch podanych liczb obliczy wynik zadanej operacji
(dodawanie, odejmowanie, mnożenie, dzielenie). W przypadku podania nieprawidłowej operacji
program ma wyświetlić odpowiedni komunikat o błędzie.

Przykładowy komunikat programu:
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 5
Podaj rodzaj operacji (+, -, *, /): +
Wynik: 10+5=15
"""

liczba_1 = float(input('Podaj pierwszą liczbę: '))
liczba_2 = float(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji (+, -, *, /): ')

if operacja == '+':
    wynik = liczba_1 + liczba_2
elif operacja == '-':
    wynik = liczba_1 - liczba_2
elif operacja == '*':
    wynik = liczba_1 * liczba_2
elif operacja == '/':
    if liczba_2 == 0:
        print('Nie mozna dzielic przez 0.')
        wynik = None
    else:
        wynik = liczba_1 / liczba_2
else:
    wynik = None

# --------------------------------------------------------------

if wynik == None:
    print('Nieprawidlowa operacja.')
else:
    print(f'Wynik: {liczba_1}{operacja}{liczba_2}={wynik}')

"""
Napisz program, który na podstawie dwóch podanych liczb obliczy wynik zadanej operacji
(dodawanie, odejmowanie, mnożenie, dzielenie). W przypadku podania nieprawidłowej operacji
program ma wyświetlić odpowiedni komunikat o błędzie.

Przykładowy komunikat programu:
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 5
Podaj rodzaj operacji (+, -, *, /): +
Wynik: 10+5=15
"""

liczba_1 = float(input('Podaj pierwszą liczbę: '))
liczba_2 = float(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji (+, -, *, /): ')

wynik = None

if operacja == '+':
    wynik = liczba_1 + liczba_2
elif operacja == '-':
    wynik = liczba_1 - liczba_2
elif operacja == '*':
    wynik = liczba_1 * liczba_2
elif operacja == '/':
    if liczba_2 != 0:
        wynik = liczba_1 / liczba_2

if wynik == None:
    print('Nieprawidlowa operacja.')
else:
    print(f'Wynik: {liczba_1}{operacja}{liczba_2}={wynik}')

"""
Napisz program obliczający kwadrat 100 pierwszych liczb całkowitych
i wypisujący wyniki na konsolę.

Przykładowe uruchomienie programu:
Kwadrat liczby 1 to 1
...
Kwadrat liczby 10 to 100
...
Kwadrat liczby 100 to 10000
"""
i = 1
while i <= 100:
    print(f'Kwadrat liczby {i} to {i ** 2}')
    # i = i + 1
    i += 1 # robi dokladnie to samo co i = i + 1, mamy tez -=, *=, /=

"""
Napisz program obliczający średnią wartość temperatury w danym tygodniu
na podstawie temperatur wprowadzonych przez użytkownika.
"""

numer_dnia = 1
suma_temperatur = 0

while numer_dnia <= 7:
    suma_temperatur += int(input(f'Podaj temperature dla dnia {numer_dnia}: '))
    numer_dnia += 1

srednia_temperatur = suma_temperatur / 7
print(f'Srednia temperatur w tym tygodniu to {srednia_temperatur:.2f}')

"""
Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10.
Użytkownik może wprowadzać komendy zmieniające położenie postaci.
Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza dobrym kierunku.
Wyjście poza planszę oznacza koniec gry.
Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.
Dodatkowo:
- po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków umieść skarb w nowym miejscu,
- z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.


ETAP 1 - ruch po planszy
1. zdefiniowane zmienne z pozycją gracza i skarbu (na razie wpisać z palca)
2. trzeba zrobić nieskończoną petle while, gdzie:
- Pokazujemy pozycje gracza
- Zapytać gracza o kierunek (w,s,a,d)
- Zmienic kierunek lub poinformowac, ze kierunek jest nieprawdlowy

ETAP 2 - Sprawdzanie pozycji gracza
1. czy gracz przemiescil sie poza plansze - jesli tak, konczymy gre
2. czy pozycja gracza (x,y) sa takie same jak pozycja skarbu (x,y) - jesli tak, komunikat o wygranej i konczymy gre

ETAP 3 - liczba krokow
1. Zdefiniować zmienna przed petla
2. Po kazdym ruchu ja zwiekszamy
3. Jeżeli gracz wejdzie na skarb, to wysiwetlamy informacje ile ruchow wykonal

ETAP 4 - podpowiedz cieplo, zimno
http://matematyka.pisz.pl/strona/1248.html
1. Policzyc odleglosc miedzy pozycja gracza a skarbu PRZED wykonaniem ruchu.
2. Po wykonaniu ruchu znow liczymy odleglosc
3. Na podstawie roznicy tych dwoch wartosci mowimy czy cieplo czy zimno.

ETAP 5 - nie wyswietlaj podpowiedzi cieplo/zimno z prawdopodobienstwem 1/5
1. uzywamy randint(1,5) i jezeli wylosuje liczbe inna niz 5, to pokazuje podpowiedz

ETAP 6 - przeniesienie skarbu po wykonaniu zbyt duzej liczby ruchow
1. Przed petla while liczymy sobie minimalna odleglosc miedzy graczem a skarbem - mozemy uzyc funkcji abs()
2. Po wykonaniu ruchu sprawdzamy czy liczba_krokow jest wieksza niz dwukrotnosc mininalnej liczby krokow
3. jezeli tak jest, to:
 - losujemy nowa pozycje skarbu (x,y),
 - liczymy na nowo minimalna liczbe krokow
 - zerujemy liczbe wykonanych przez gracza krokow

ETAP 7 - losowanie pozycji gracza i pozycji skarbu na samym poczatku gry
1. Dodać randint przy tworzeniu zmiennych przed petla while
"""
import math
import random

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

while True:
    print(f'Twoja pozycja x={gracz_x} y={gracz_y}')
    odleglosc_przed_ruchem = math.sqrt((skarb_x-gracz_x)**2 + (skarb_y-gracz_y)**2)

   # ruch gracza
    kierunek = input('Podaj kierunek (w, s, a, d): ')
    if kierunek == 'w':
        gracz_y += 1
    elif kierunek == 's':
        gracz_y -= 1
    elif kierunek == 'a':
        gracz_x -= 1
    elif kierunek == 'd':
        gracz_x += 1
    else:
        print('Nieprawidlowy kierunek')
        continue

    odleglosc_po_ruchu = math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)

    # sprawdzenie czy gracz wyszedl poza plansza
    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print('Jestes poza plansza! GAME OVER!!!')
        break

    # sprawdzenie czy gracz znalazl skarb
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print('BRAWO! WYGRALES! Znalazles skarb')
        break

    if random.randint(1, 5) != 5:
        if odleglosc_po_ruchu < odleglosc_przed_ruchem:
           print('cieplo')
        else:
           print('zimno')

# KOLEKCJE

liczba = 10  # pojedyncza wartosc

# Tupla, krotka (ang. tuple)

#    0   1   2 - indeks
a = (10, 20, 30)
print(type(a))
print(a)

# operator dostepu
print(a[0])

print('-' * 60)

a = (10, True, 'Ala ma kota')
print(a[0])
print(a[1])
print(a[2])
# print(min(a))

print('-' * 60)

a = (10, 20, 30)
print(len(a))
print(min(a))
print(max(a))
print(min(a))
print(sum(a))

print('-' * 60)

# operator dostepu - "na sterydach"
#    0    1    2    3    4    5    6    7    8    9
a = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
#    -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

# a[start:stop-1:krok]
print(a)
print(a[0])
print(a[1])
print(a[0:2])  # ('a', 'b'), indeksy 0, 1; przedzial lewostronnie domkniety, prawostronnie otwarty
print(a[1:5])  # ('b', 'c', 'd', 'e')
print(a[5:])  # ('f', 'g', 'h', 'i', 'j'), od indeksu 5 do konca
print(a[:5])  # ('a', 'b', 'c', 'd', 'e'), od poczatku do 4 wlacznie (bez 5)
print(a[:])  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
i = 1
print(a[i])  # b
print(a[-1])  # j
print(a[-5:-2])  # ('f', 'g', 'h')
print(a[-2:-5])  # () - pusta tupla
print(a[0:-1])  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
print(a[-3:])  # ('h', 'i', 'j')
print(a[::2])  # ('a', 'c', 'e', 'g', 'i')
print(a[::-25])  # ('j',)
print(a[::25])  # ('a',)
print(a[::-2])  # ('j', 'h', 'f', 'd', 'b')
print(a[::-1])  # ('j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')\

print('j' in a)  # True, czy 'j' zawiera sie w kolekcji a
print('j' not in a)  # False, czy 'j' NIE zawiera w kolekcji a

print('-' * 60)

tupla_a = (1, 2, 3)
tupla_b = (4, 5, 6)

tupla_c = tupla_a + tupla_b
print(tupla_c)

tupla_d = tupla_b + tupla_a
print(tupla_d)

tupla_e = tupla_a * 5
print(tupla_e)

print(tupla_e[0])
# tupla_e[0] = 123  # TypeError: 'tuple' object does not support item assignment

print('-' * 60)

# LISTA

lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(type(lista_a))

print(lista_a[0])
print(lista_a[0:3])

lista_a[0] = 11
print(lista_a)

lista_a.append(110)  # dodaje element na koniec listy
print(lista_a)

lista_a.insert(3, 35)
print(lista_a)

lista_a[0:2] = [1, 2]
print(lista_a)

lista_a[0:3] = [1, 2]
print(lista_a)


lista_a[0:2] = [1000, 2000, 3000]
print(lista_a)

print('-' * 60)

i = 1
while i < 3:
    print(i)
    # break
    i += 1
else:
    # to co jest w tym else wykona sie tylko wtedy, kiedy nie przerwe
    # petli za pomoca break
    print('Else po while')


print('-' * 60)


lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
while i < len(lista_a):
    print(lista_a[i])
    i += 1

print('-' * 60)

# to samo, ale przy uzciu petli for
lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for liczba in lista_a:  # element - zmienna tymczasowa, ja ustalam jak sie nazywa
    print(liczba)

print('-' * 60)

# range()

for liczba in range(-2, 3):  # lewostronnie domkniety, prawostronnie otwarty
    print(liczba)

print('-' * 60)

for liczba in range(-10, 11, 2):
    print(liczba)

"""
Stwórz tuplę zawierającą 10 różnych liczb całkowitych.
Korzystając z operatora dostępu oraz wycinania pobierz:
- drugi element
- przedostatni element
- elementy od trzeciego do siódmego (włącznie)
- co trzeci element
- co drugi element licząc od końca
"""

#    0   1   2   3   4   5   6   7   8   9 -> klucze
x = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
#    1   2   3   4   5   6   7   8   9   10 -> który element
#   -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 -> ideksy ujemne

print(x[1])  # 20
print(x[8])  # 90
print(x[-2])  # 90
print(x[2:7])  # 30, 40, 50, 60, 70
print(x[::3])  # 10, 40, 70, 100
print(x[::-2])  # 100, 80, 60, 40, 20




"""
Napisz program obliczający średnią wartość z podanych przez użytkownika liczb.
Do przechowywania liczb użyj listy. Pozwól na wprowadzenie 10 liczb.
Skorzystaj z funkcji wbudowanej sum().
"""

liczby = []  # [] - tworzy pusta liste

i = 1
while i <= 10:
    i += 1
    liczba = int(input('Podaj liczbe: '))
    liczby.append(liczba)

srednia = sum(liczby) / len(liczby)
print(f'Srednia z prowadzonych liczb {liczby} to {srednia:.2f}')

"""
Napisz program obliczający średnią wartość z podanych przez użytkownika liczb.
Do przechowywania liczb użyj listy. Pozwól na wprowadzenie 10 liczb.
Skorzystaj z funkcji wbudowanej sum().
"""

liczby = []  # [] - tworzy pusta liste

while len(liczby) < 10:
    liczba = int(input('Podaj liczbe: '))
    liczby.append(liczba)

srednia = sum(liczby) / len(liczby)
print(f'Srednia z prowadzonych liczb {liczby} to {srednia:.2f}')
"""
Napisz program zliczający wystąpienia liczb dodatnich i ujemnych w zadanej
liście liczb całkowitych.
"""

# https://pl.wikipedia.org/wiki/Znak_liczby

liczby = [1, 2, 3, -100, -10, 0, 4]

dodatnie = 0
ujemne = 0

for liczba in liczby:
    if liczba > 0:
        dodatnie += 1
    elif liczba < 0:
        ujemne += 1

print(f'Dodatnich: {dodatnie}')
print(f'Ujemnych: {ujemne}')

"""
Napisz program wypisujący wszystkie liczby od 0 do 100,
podzielne przez 3 lub podzielne przez 5. Wypisz także jak dużo
takich liczb wystąpiło w tym przedziale.

Liczby podzielne przez 3 lub 5:
0
3
5
...
96
99
100
W przedziale 0-100 jest 48 liczb podzielnych przez 3 lub 5
"""
ile_liczb = 0
for liczba in range(0, 101):
    if liczba % 3 == 0 or liczba % 5 == 0:
        print(liczba)
        ile_liczb += 1

print(f'W przedziale 0-100 jest {ile_liczb} liczb podzielnych przez 3 lub 5')


"""
Wypisz liczby od 1 do 100, przy czym:
- liczby podzielne przez 3 zastąp słowem 'Fizz',
- liczby podzielne przez 5, zastąp słowem 'Buzz',
- natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem 'FizzBuzz'.
"""
for liczba in range(1, 101):
    if liczba % 3 == 0 and liczba % 5 == 0:
        print('FizzBuzz')
    elif liczba % 3 == 0:
        print('Buzz')
    elif liczba % 5 == 0:
        print('Fizz')
    else:
        print(liczba)













