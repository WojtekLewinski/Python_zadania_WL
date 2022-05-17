print("_" * 65, "funkcje - podstawowe ionformacje ")
# # fukcja ma nazwe oraz nawiasy okrągłe
# print('Ala ma kota')
#
# # funkcja składa sie z sygnatury oraz ciała funkcji
# def powiedz_czesc():# ta część nazywa sie sygnatura: zaczynamy od def żeby python wiecział że definiujesz nową funkcję. /
# # Mamy nawiady okrągłe i między nimi możemy podać argumenty
#     print('cześć')# druga część nazywa się ciałem funkcji zaczyna się od wcięcia żeby python wiedział że przynależy do funkcji
#
# # funkcja zadziała dopiero kiedy ją uruchomimny :
# powiedz_czesc()
#
print("_" * 65, "przykłady")
# def srednia(liczba1, liczba2):
#     c = (liczba1+liczba2) / 2
#     print(c)
#
# srednia(10,7)
#
# def srednia_z_listy(lista_liczb):
#     wynik = sum(lista_liczb)/len(lista_liczb)
#     print(wynik)
#
# srednia_z_listy([10,20,30]) # mozna podać listę
# srednia_z_listy({1,2,3})# mozna podać zbiór
#
print("_" * 65, "funkcja moze coś zwrócić _ return")

def srednia_z_wielu(liczby):
    wynik = sum(liczby)/len(liczby)
    return wynik  #return powoduje przerywanie funkcji i nic co zostanie wpisane potem nie zostanie wykonane ani wyświetlone

policzona_srednia = srednia_z_wielu([10,20,30])
print(policzona_srednia)

# return moze zwrócić więcej wartości jako tuplę
def dodawanie_mnożenia(liczba_1, liczba_2):
    return (liczba_1+liczba_2, liczba_1*liczba_2)
wynik = dodawanie_mnożenia(2.5,3)
print(wynik)

# można rozkapkować tuplę na klucz i wartość
wynik_dodawania,wynik_mnozenia = dodawanie_mnożenia(4,5)
print(wynik_mnozenia)
print(wynik_dodawania)
#
#
print("_" * 65, " dokumentacja, jak dokumentować swoje funkcje ")
#
# # type-hinting czyli podpowiadanie typów. Jest to tylko sugestia bo pthon jest słabotypowalny i można dodawać prawie wszystko Chodzi bardziej o naprwadznei użytkownika na prawidłowy typ
# # def dodawanie(liczba1: int, liczba2: int)-> int: # dodanie do ciała funkcji dwukropka mówi jakiego typu powinien być agrument. znaczek -> po funkcji a przed dwukropkiem daje znać co zwróci funkcja.
# # => jest to tylko podpowiedź a nie wymóg, mozesz wprowadzić inne typy ale funkcja moze świecić siena żóto jako ostrzeznei
# #     return liczba1 + liczba2
#
# # wynik= dodawanie(2,3) # można do siebie dodać dwie listy ale nie dwa zbiory [1,2,3]+ [3,4,5] da nam [1,2,3,4,5,6].
# # # na zbiorach nie działa operator dodawania.
# # print(wynik)
#
# #docstring -tekstowy opis co nasz funkcja robi. przykłąd poniżej:
#
# def dodawanie(liczba1, liczba2):
#     """
#     Funkcja dodaje do siebie dwa podane przez uzytkownika argumenty:
#
#     :param liczba1:pierwsza liczba podana przez użytkownika
#     :param liczba2: druga liczba podana przez użytkownika
#     :return: suma liczby  pierwszej i drugiej
#     """
#     return liczba1 + liczba2
#
print("_" * 65, " zadanie")
# """
# Stwórz kalkulator oparty o funkcje:
# 1. Pobierz od użytkownika 2 liczby
# 2. Zapytaj o działanie: (+, -, *, /)
# 3. Na podstawie działania wykonujemy obliczenia i je pokazujemy
# """
#

# a = float(input('podaj pierszą liczbę'))
# b = float(input('podaj drugą liczbe'))
# c = input('podaj działanie jakie chcesz wykonać (+, -, *, /)')
# def operacja(a,b):
#     if c =='+':
#         wynik = a + b
#         return wynik
#     elif c == '-':
#         wynik = a - b
#         return wynik
#     elif c =='*':
#         wynik = a * b
#         return wynik
#     elif c == '/':
#         wynik = a / b
#         return wynik
# e = operacja(a,b)
# print(e)

print("_" * 65, " kolejne zadanie")
"""
# Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą.
# Przykład użycia:
# > czy_jest_pierwsza(10)
# False
# > czy_jest_pierwsza(17)
# True
# 
# Liczba pierwsza
# - bedzie intem
# - wieksza od 1
# - dzieli sie tylko przez 1 i przez sama siebie
# """
# #liczba = print('podaj dowolną liczbą całkowitą:')
# def czy_liczba_pierwsza(liczba:int)->bool:
#     if liczba <= 1:
#         return False
#     for a in range(2,liczba):
#         if liczba % a == 0:
#             return False
#     return True
# wynik = czy_liczba_pierwsza(15)
# print(wynik)
#
# print("_" * 65, " testowanie funkcji")
# # jak chcenmy używać pytesta to funkcje testowe musza się zaczynać od "test_"
#
# #assert - asercja
# def test_przykladowy():
#     assert czy_liczba_pierwsza(-5) == False
#
# # podejście gwT given when then
#
#     liczba = -5 # given
#     wynik = czy_liczba_pierwsza(liczba) # when
#     assert wynik == False # then
#
# def test_liczb_pierwszych():
#      liczby_pierwsze = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#      for liczby in liczby_pierwsze:
#          assert czy_liczba_pierwsza(liczby) == True
#
# def test_liczb_niepierwszych():
#     liczby_niepeirwsze = [-100,-10,-1,0,1,4,9,15,24,36,100]
#     for liczba in liczby_niepeirwsze:
#         assert czy_liczba_pierwsza(liczba) == False

print("_" * 65)

""" kolejne zadanie 3 

Napisz funkcję zwracającą zbiór wszystkich znaków
występujących w napisie więcej niż zadana liczba razy.
Przykład użycia:
> wiecej_niz('ala ma kota a kot ma ale', 3) {'a', ' '}

1. Definiujemy funkcje
2. Policzyc ile jest znakow (.count()) i dodac je do zbioru,
ktory na koncu zwracamy

Przypadki testowe?
pusty napis
2 dowolne napisy
"""

# TDD -Test Driven Development

# def wiecej_niz(napis: str, ile_znakow: int) ->set:
#     wystapienia = {}# definiujesz zbiór
#     for litera in napis.lower(): #w każdym obrocie zmiennej literamam yamła literę i sprawdzamy czy występuje w słowniku wystąpienia
#         if litera not in wystapienia:
#             wystapienia[litera] = 1
#         else:
#             wystapienia[litera]+=1
#
#     wynik = set() # przygotowujemy zbiór do wklejenia wyników
#     for litera, liczba_wystapien in wystapienia.items():
#         if liczba_wystapien > ile_znakow:# sprawdza czy liczba wystąpień litery jest większa niz liczba znaków podana przez usera
#             wynik.add(litera)
#     return wynik
#
# print(wiecej_niz('ala ma kota a kot ma ale',3))

#
x = "ala ma kota kot ma alę" # mamy napis w którym chcemy sprawdzić ile razy występuje każda litera
wystapienia = {} # tworzymy zbiór w który będziemy wrzucać klucz i wartość
for litera in x: #pętla  ma po kolei brać literę z "x" i
    if litera not in wystapienia:# jeżlei iltera nie wystęuje jeszcze  zbirze wystąpnia to zostaje dodana z wartościa 1
        wystapienia[litera] = 1
    else: # jeżeli odpalony zostaje ten warunek oznacza że litera już wydtępuje /
        # i dlatego nie zostaje dodana ponowne a jesynie zwiększamy jej wartość o jeden
        wystapienia[litera] +=1
print(wystapienia)




print("_" * 65, " funkcje mogą mieć wartość domyślną")
# w sygnaturze można dopisać wartości domyślne np liczba2: int =2):
#     c = (liczba1+liczba2) / 2
def srednia(liczba1: int, liczba2: int =2):
    c = (liczba1+liczba2) / 2
    print(c)

srednia(10,)

# w powyższym przykładzie funkcja średnia ma dwa warunki jeden obowiązkowy i drugi domyślny ustawiony na cyfrę dwa, dlatego średnia wychodzi 6
# zasada jest taka że w ciele funkcji podajemy najpierw wartosći obowiązkowe a potem domyślne
