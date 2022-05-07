"""Napisz program sprawdzający czy podana przez użytkownika liczba:
- jest nieparzysta, podzielna przez 3 i większa od 10
- lub jest to liczba 7.
"""

liczba = int(input("podaj dowolną liczbę"))
print(f'czy jest nieparzysta podzielna przez 3 i większa od 10' + f'{liczba % 2 > 0 and liczba % 3 == 0 and liczba > 10 }')
print(f'czy jest to liczba 7: {liczba ==7}')

"""
Napisz program sprawdzający czy podana przez użytkownika liczba jest:
- większa od 10
- mniejsza równa 15
- podzielna przez 2 (użyj operatora modulo)

Przykładowy komunikat programu:
Podaj liczbę: 15
Większa od 10: True
Mniejsza równa 15: True
Podzielna przez 2: False
"""

liczba_użytkownika = int(input("podaj liczbę"))
print(f'Czy liczba jest wieksza od 10: {liczba_użytkownika>10}',
      f'\nCzy liczba jest mniejsza lub równa 15?: {liczba_użytkownika<=15}',
      f'\nCzy liczba jest podzielna przez 2: {liczba_użytkownika%2==0}')

"""
Stwórz tuplę zawierającą 10 różnych liczb całkowitych.
Korzystając z operatora dostępu oraz wycinania pobierz:
- drugi element
- przedostatni element
- elementy od trzeciego do siódmego (włącznie)
- co trzeci element
- co drugi element licząc od końca
"""

# #    0   1   2   3   4   5   6   7   8   9 -> klucze
# x = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# #    1   2   3   4   5   6   7   8   9   10 -> który element
# #   -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 -> ideksy ujemne
# print(x [1])
# print(x [-2])
# print(x [2:8])
# print(x [::3])
# print(x [::-2])

"""
Napisz program obliczający średnią wartość z podanych przez użytkownika liczb.
Do przechowywania liczb użyj listy. Pozwól na wprowadzenie maksymalnie 10 liczb.
Skorzystaj z funkcji wbudowanej sum().
"""


# lista_a = []
# i=1
# while i <= 10:
#     liczba = float(input("Podaj liczbę"))
#     lista_a.append(liczba)
#     i += 1
#     srednia = sum(lista_a) / len(lista_a)
# print(f'Średnia z wprowadzonych liczb: {srednia:.2f}')


# i=1
# lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# while i < len(lista_a):
#     print(lista_a[i])
#     i+=1


# lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for element in lista_a:
#     print(element)

"""
Napisz program zliczający wystąpienia liczb dodatnich
i ujemnych w zadanej liście liczb całkowitych.
"""

# https://pl.wikipedia.org/wiki/Znak_liczby

# liczby = [1, 2, 3, -100, -10, 0, 4]
# dod = 0
# uje = 0
# zero = 0
# for lista   in liczby:
#     if lista > 0:
#         dod += 1
#     elif lista < 0:
#         uje += 1
#     else:
#         zero +=1
# print(f'dodatnie:{dod}, ujemne {uje} zero {zero}')
#

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


# lista_a = []
# for liczba in range(0,101):
#     if liczba % 3 == 0 or liczba % 5 == 0:
#         print(liczba)
#         lista_a.append(liczba)
# print(f'liczby od 1 do 100 podzielne przez 3 lub 5: {len(lista_a)}')


"""
Wypisz liczby od 1 do 100, przy czym:
- liczby podzielne przez 3 zastąp słowem 'Fizz',
- liczby podzielne przez 5, zastąp słowem 'Buzz',
- natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem 'FizzBuzz'.
"""

for zakres in range (1,101):
    if zakres % 3 == 0 and zakres % 5==0:
        print("fizbauzz")

badanie = int(input("W skali od 1 do 10 jak bardzo poleciłbys szkolenie w ALX"))

if badanie >= 9:
    print("promotorzy")

if badanie >=7 and badanie <9:
    print("neutralni")

if badanie <=6:
    print("detraktorzy")

badanie = int(input("W skali od 1 do 10 jak bardzo poleciłbys szkolenie w ALX: "))

if badanie >= 1 and badanie <= 10:
    if badanie >= 9:
        print("promotorzy")
    elif badanie >= 7:
        print("neutralni")
    else:
        print("detraktorzy")
else:
    print('Podaj wartosc z zakresu 1-10')
""""""


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
Napisz program, który na podstawie wprowadzonych wymiarów opakowania (x, y, z) obliczy
jego objętość oraz sprawdzi, czy jest ona większa od 1 litra (1000 cm3).
"""

# wysokosc = float(input("podaj wysokość w cm"))
# szerokosc = float(input("podaj szerokość w cm"))
# długosc = float(input("podaj długość w cm"))
# wymiar = wysokosc * szerokosc * długosc
# print(f'czy objętość jest większa od 1000cm3 {wymiar > 1000}')

# Badanie = int(input("W skali od 1 do 10 jak bardzo poleciłbyś szkolenie w ALX"))
# if Badanie >= 9:
#     print("promotorzy")
# elif Badanie >=7:
#     print("neutralni")
# else:
#     print("detraktorzy")

"""
Napisz program, który zapyta uzytkownika o liczbę całkowitą.
Jeżeli uzytkownik poda liczbę 10, wtedy wyświetl komunikat:
Podałeś szczęśliwy numerek! Wygrałeś!
W przeciwnym wypadku wyświetl:
Spróbuj jeszcze raz!
"""

# liczba = int(input("podaj liczbę całkowitą od 1 do 10"))
# if liczba == 10:
#     print("Podałeś szczęśliwy numerek! Wygrałeś!")
# else:
#     print("Spróbuj jeszcze raz!")



"""
Napisz program, który sprawdzi pełnoletność osoby na podstawie roku jej urodzenia.

Przykładowy komunikat programu:
Podaj rok urodzenia: 1980
Jesteś pełnoletni!
"""
# import datetime
# rok = int(input("podaj rok urodzenia"))
# akatualny_rok = datetime.date.today().year
# wiek = akatualny_rok - rok
# if wiek >= 18:
#     print("jesteś pełnoletni!")
# else:
#     print("wypad ze sklepu")


"""
Napisz program, który na podstawie dwóch podanych liczb obliczy wynik zadanej operacji
(dodawanie, odejmowanie, mnożenie, dzielenie). W przypadku podania nieprawidłowej operacji
program ma wyświetlić odpowiedni komunikat o błędzie.

Przykładowy komunikat programu:
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 5
Podaj rodzaj operacji (+, -, *, /): +
Wynik: 15
"""
# pierwsza_liczba = float(input("podaj pierwszą liczbę"))
# druga_liczba  = float(input("podaj drugą liczbę"))
# opracja = input("podaj operację +,-,*,/")
#
# if opracja == '*':
#     wynik = pierwsza_liczba * druga_liczba
# elif opracja == '+':
#     wynik = pierwsza_liczba + druga_liczba
# elif opracja == '-':
#     wynik = pierwsza_liczba - druga_liczba
# elif opracja == '/':
#     wynik = pierwsza_liczba / druga_liczba
# else:
#     print("błędne działanie")
# print(wynik)



# liczba = 1
# while liczba <= 100:
#  print(liczba)
#  liczba = liczba + 1


"""
Napisz program obliczający kwadrat 100 pierwszych liczb całkowitych
i wypisujący wyniki na konsolę.

Przykładowe uruchomienie programu:
...
Kwadrat liczby 10 to 100
"""

# liczba = 1
# while liczba <= 100:
#  print(f'Kwadrat liczby {liczba**2}')
#  liczba += 1


"""
Napisz program obliczający średnią wartość temperatury w danym tygodniu
na podstawie temperatur wprowadzonych przez użytkownika.
"""



i = 1
lista_a= []
while i <= 7:
  temperatura = float(input("podaj temperaturę"))
  lista_a.append(temperatura)
  i+= 1
srednia = sum(lista_a) / 7
print(srednia)



#
# a = [0,1,2,3,4,5,6,7]
# print(a[::7])
# print(0 in a)

# tupla_a = [1,2,3]
# tupla_b = [4,5,6]
# tupla_c =  tupla_a + tupla_b
# tupla_d = tupla_a *5
# print(tupla_d)

# LIsta

lista_a = [10,20,30,40,50,60,70,80,90,100]
print(type(lista_a))



