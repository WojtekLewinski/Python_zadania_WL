"""
Napisz program wypisujący na konsolę tabliczkę mnożenia
dla liczb od 0 do 10 w postaci tabelki.

       0   1   2   3   4   5   6   7   8   9  10

0      0   0   0   0   0   0   0   0   0   0   0
1      0   1   2   3   4   5   6   7   8   9  10
2      0   2   4   6   8  10  12  14  16  18  20
3      0   3   6   9  12  15  18  21  24  27  30
4      0   4   8  12  16  20  24  28  32  36  40
5      0   5  10  15  20  25  30  35  40  45  50
6      0   6  12  18  24  30  36  42  48  54  60
7      0   7  14  21  28  35  42  49  56  63  70
8      0   8  16  24  32  40  48  56  64  72  80
9      0   9  18  27  36  45  54  63  72  81  90
10     0  10  20  30  40  50  60  70  80  90 100
"""
""" poniżej moja propozycja """
# zmienna_a = 0
# zmienna_b = 0
# while zmienna_a < 10:
#     zmienna_a * zmienna_b
#     zmienna_a =zmienna_a +1
#     print(zmienna_a)

"""robione na zajęciach"""
# print(" "*5, end=" ")
# for a in range(0,11):
#     print(f'{a:5}', end=' ')
# print()
# print()
#
# for x in range(0, 11):
#     print(f'{x:<5}',end=" ")
#     for y in range(0,11):
#         print(f'{x * y:5}', end=' ')
#     print()


print("_"*65, "nowe zadanie")

# """ enumeracja zaczyna od 0 i wyświetla wartość """
# temperatura = [10,15,17,-1,-5,0,2]
# for temperatura in enumerate(temperatura):
#     print(f'index: {temperatura[0]}, wartość: {temperatura[1]}')

"""mozna przypisywać wartości bezpośrednio do tupli lub listy. przykład poniżej.
 Liczba zmiennych i liczba elementów musi być taka sama inaczej dostajemy błąd"""
# imie,nazwisko,wiek= ('Wojciech','Lewinski', '45')
# print(imie)
# print(nazwisko)
# print(wiek)


# """wykorzytanie rozpakowania na poprzednim przykładzie temperatur"""
# temperatura = [10,15,17,-1,-5,0,2]
# for indeks, temperatura in enumerate(temperatura):
#     print(f'index: {indeks}, wartość: {temperatura}')

print("_"*65, "nowe zadanie")

# """oerator dostępu"""
# napis= 'Ala ma kota kot ma kompiolator'
# print(napis)
# print(napis[0:10])
# print(napis[0:10:2])#co drugi znak od 0 do 10
# print(napis[::-1]) # od tyłu i przydaje siędo sprawdzenia czy zdanei jest palindromem
# print(napis.upper())# wielkie litery
# print(napis.lower())# małe liter
# print(napis.capitalize())# zmienia pierwszą literę na wielką a wszystkie pozostałe na małe.
# # jeżeli w zdaniu jest kropka od nowego zdania nie zmienia na wwielkie
# print(napis.title())# każde słowo z dużej litery
# print(napis.split())# kroi zdanie na sekcje i możemy podać jaki znak będzie separatorem
#
# slowa= napis.split()
# print(slowa)
# print(slowa[0:3]) # ['Ala', 'ma', 'kota']
#
# print("_"*65, "nowe zadanie")
# """scalanie wartości ale nie kontatenacja """
# po_scaleniu = '<....>'. join(['a','b','c']) # używasz łćzanika w naszym przypadku ..., następnie join + kolekcj. Kolekcjka może być lista lub tupla
# print(po_scaleniu)
#
# po_scaleniu = '<....>'.join('ala ma kota') # możesz dodać tuplę zawierającą zapis
# print(po_scaleniu)
#
# a = ['1','2','3']
# po_scaleniu = '<....>'.join(a)
# print(po_scaleniu) # możesz przypisać wartość do zmiennej i zastosować zmienną do łaćznia
#
# print(napis)
# print(napis.count('a')) #licza wystąpienia wpisanego znaku
# print(napis.index('a')) # podaje nr indeksu wystąpnienia pierwszej literki a./
# # Python szuka dokładnie takiego znaku jaki wpisaliśmny więc podaj 2 - małe a występuje jako 3
#
# """oba poniższe robią dokładnie to samo. Podają nr indeksu znaku który wyszukujemy. Różnia sięzachowaniem kiedy nie znajdą znaku"""
# # print(napis.index('z'))# jeżeli nie znajdzie znaku wyrzuca błąd ValueError: substring not found
# print(napis.find('z')) # szuka znaku, napisu, jeżeli nie znajdzie wyrzuci "-1"
#
# print(napis.replace("a",'*')) # zastępuje podany w pierwszej wartości znak na podany przez nas w drugiej wartośći

print("_"*65, "nowe zadanie")

"""
Napisz program zliczający liczbę wystąpień samogłosek (a, e, i, o, u, y)
w podanym przez użytkownika napisie.

1. Pobieramy napis od użytkownika
2. Przechodzimy po kazdej literze z napisu (for)
3. Sprawdzamy czy znak znajduje sie w samogloskach -> tak? to go zliczamy

Jak poradzić sobie ze zliczaniem dużych liter?
1. Możemy je dodać do tupli z samogłoskami
2. Użyć metody .lower()
"""

samogloski = ['a','e','i','o','u','y']
tekst = input('Wpisz dowolny tekst:')
ile_samoglosek = 0
for litera in tekst:
    if litera in samogloski:
        ile_samoglosek += 1
print(f'w napisie {tekst} znajduje sie {ile_samoglosek} samogłosek')


