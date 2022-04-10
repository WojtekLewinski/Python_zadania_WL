# # operatory arytmetyczne
# import math
#
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)  # dzielenie calkowitoliczbowe
# print(10 ** 3)
# print(9 ** 0.5)
# print(10 % 3)  # modulo, reszta z dzielenia
#
# # operatory porownania - daje nam True albo False
# print(1 == 1)  # True, a rowne b
# print(1.0 == 1)  # True
# print("1" == 1)  # False
# print(int("1") == 1)  # True
# print(1 != 1)  # False, a rozne od b
# print(1 > 1)  # False, a wieksze od b
# print(1 >= 1)  # True, a wieksza badz rowne b
# print(1 < 1)  # False
# print(1 <= 1)  # True
#
# # operatory logiczne
# print(True and True)  # True, i, koniunkcja
# print(True or False)  # True, lub, alternatywa
# print(not True)  # False, przeczenie
#
# round(1.25)# zaokręglenie
#
#
#
# # KOLEKCJE
#
# liczba = 10  # pojedyncza wartosc
#
# # Tupla, krotka (ang. tuple)
#
# #    0   1   2 - indeks
# a = (10, 20, 30)
# print(type(a))
# print(a)
#
# # operator dostepu
# print(a[0])
#
# print('-' * 60)
#
# a = (10, True, 'Ala ma kota')
# print(a[0])
# print(a[1])
# print(a[2])
# # print(min(a))
#
# print('-' * 60)
#
# a = (10, 20, 30)
# print(len(a))
# print(min(a))
# print(max(a))
# print(min(a))
# print(sum(a))
#
# print('-' * 60)
#
# # operator dostepu - "na sterydach"
# #    0    1    2    3    4    5    6    7    8    9
# a = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# #    -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
#
# # a[start:stop-1:krok]
# print(a)
# print(a[0])
# print(a[1])
# print(a[0:2])  # ('a', 'b'), indeksy 0, 1; przedzial lewostronnie domkniety, prawostronnie otwarty
# print(a[1:5])  # ('b', 'c', 'd', 'e')
# print(a[5:])  # ('f', 'g', 'h', 'i', 'j'), od indeksu 5 do konca
# print(a[:5])  # ('a', 'b', 'c', 'd', 'e'), od poczatku do 4 wlacznie (bez 5)
# print(a[:])  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# i = 1
# print(a[i])  # b
# print(a[-1])  # j
# print(a[-5:-2])  # ('f', 'g', 'h')
# print(a[-2:-5])  # () - pusta tupla
# print(a[0:-1])  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
# print(a[-3:])  # ('h', 'i', 'j')
# print(a[::2])  # ('a', 'c', 'e', 'g', 'i')
# print(a[::-25])  # ('j',)
# print(a[::25])  # ('a',)
# print(a[::-2])  # ('j', 'h', 'f', 'd', 'b')
# print(a[::-1])  # ('j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')\
#
# print('j' in a)  # True, czy 'j' zawiera sie w kolekcji a
# print('j' not in a)  # False, czy 'j' NIE zawiera w kolekcji a
#
# print('-' * 60)
#
# tupla_a = (1, 2, 3)
# tupla_b = (4, 5, 6)
#
# tupla_c = tupla_a + tupla_b
# print(tupla_c)
#
# tupla_d = tupla_b + tupla_a
# print(tupla_d)
#
# tupla_e = tupla_a * 5
# print(tupla_e)
#
# print(tupla_e[0])
# # tupla_e[0] = 123  # TypeError: 'tuple' object does not support item assignment
#
# print('-' * 60)
#
# # LISTA
#
# lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(type(lista_a))
#
# print(lista_a[0])
# print(lista_a[0:3])
#
# lista_a[0] = 11
# print(lista_a)
#
# lista_a.append(110)  # dodaje element na koniec listy
# print(lista_a)
#
# lista_a.insert(3, 35)
# print(lista_a)
#
# lista_a[0:2] = [1, 2]
# print(lista_a)
#
# lista_a[0:3] = [1, 2]
# print(lista_a)
#
#
# lista_a[0:2] = [1000, 2000, 3000]
# print(lista_a)
#
# print('-' * 60)
#
# i = 1
# while i < 3:
#     print(i)
#     # break
#     i += 1
# else:
#     # to co jest w tym else wykona sie tylko wtedy, kiedy nie przerwe
#     # petli za pomoca break
#     print('Else po while')
#
#
# print('-' * 60)
#
#
# lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# i = 0
# while i < len(lista_a):
#     print(lista_a[i])
#     i += 1
#
# print('-' * 60)
#
# # to samo, ale przy uzciu petli for
# lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for liczba in lista_a:  # element - zmienna tymczasowa, ja ustalam jak sie nazywa
#     print(liczba)
#
# print('-' * 60)
#
# # range()
#
# for liczba in range(-2, 3):  # lewostronnie domkniety, prawostronnie otwarty
#     print(liczba)
#
# print('-' * 60)
#
# for liczba in range(-10, 11, 2):
#     print(liczba)
#
# # """oerator dostępu"""
# # napis= 'Ala ma kota kot ma kompiolator'
# # print(napis)
# # print(napis[0:10])
# # print(napis[0:10:2])#co drugi znak od 0 do 10
# # print(napis[::-1]) # od tyłu i przydaje siędo sprawdzenia czy zdanei jest palindromem
# # print(napis.upper())# wielkie litery
# # print(napis.lower())# małe liter
# # print(napis.capitalize())# zmienia pierwszą literę na wielką a wszystkie pozostałe na małe.
# # # jeżeli w zdaniu jest kropka od nowego zdania nie zmienia na wwielkie
# # print(napis.title())# każde słowo z dużej litery
# # print(napis.split())# kroi zdanie na sekcje i możemy podać jaki znak będzie separatorem
#
#
# #round(2.5) zaokrągla na zasadach ogólnych
# #math.floor(2.5) zaokrągla w dół
# #math.ceil(2.5) zaokrągla w górę
# #math.sqrt(4)
#

