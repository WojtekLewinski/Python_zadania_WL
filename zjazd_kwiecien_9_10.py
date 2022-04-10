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


# print("_"*65, "nowy temat enumeration")
#
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

print("_"*65, "nowy temat operatory dostępu")

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

# samogloski = ['a','e','i','o','u','y']
# tekst = input('Wpisz dowolny tekst:')
# ile_samoglosek = 0
# for litera in tekst:
#     if litera in samogloski:
#         ile_samoglosek += 1
# print(f'w napisie {tekst} znajduje sie {ile_samoglosek} samogłosek')


"""
Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie
pomiędzy nawiasami <>. Nawiasy mogą wystąpić tylko raz.

Przykład:
Ala ma <kota>, a kot ma Alę
4


1. Sprawdzam liczbę < i > - powinno ich być po jednym,
      jeżeli liczba tych nawiasów jest inna, to kończę program
2. W pętli sprawdzam czy:
      - mam zliczac
      - mam przestać zliczać
      - czy zliczanie jest włączone i wtedy zliczam
"""

# napis = input("podaj napis: ")
# lista1 = napis.split("<")
# lista2 = lista1[1].split('>')
# wyraz = lista2[0]
# liczba_znakow = 0
# for znak in wyraz:
#     liczba_znakow += 1
# print(f'liczba znaków w <> wynosi: {liczba_znakow}')


# napis = input("podaj napis: ")
# if napis.count('<') != 1 or napis.count('>') != 1:
#     print('wpisałeś błędne dane')
#     exit()
# a = napis.find('<')
# b = napis.find('>')
# c = b - a -1
# if c > 0:
#     print(c)
# else:
#     print('podałeś błędna kolejnośc znaków<>')


print("_" * 65, "nowy temat słowniki")

# Słowniki dic - z ang Dictionary. Słowniki mają klucz oraz wartość. /
# Jest mutowalny wiec mozna go edytować/. Wartość może być czymkolwiek. INT, napis, lista, tupla, inny słownik./
# Klucz nie może być listą, może być kazdą wartościąktóra jest haszowalna, posiada metodę hasz czyli posiada metodę Float, int, tupla, boolean

#
# slownik = {
#     'piotr' : 200,
#     'adam': 203,
#     'kasia': 187,
#     1: 555,
# }
# print(slownik)
# print(slownik['piotr'])
# print(slownik[1])
# print(slownik.get("krystyna"))
# print(slownik.keys()) # zwraca listę wszystkich kluczy ze słownika
# print(slownik.values())# zwraca listę wszystkich wartości ze słownika
# print(slownik.items())# otrzymujemy listę tupli z dwoma wartościami pierwsza to klucz druga to wartość
# print(list(slownik.items())[1][1])



print("_" * 65, "zadanie ze słowników ")
"""
Napisz program wyliczający kwotę należną za zakupiony towar
na podstawie podanej przez użytkownika wagi i nazwy produktu.
Do przechowywania informacji o cenie za kilogram
danego produktu użyj słownika.
Wypisz wszystkie dostępne produkty w sklepie.


1. Robimy słownik z produktami, dodajmy:
      ziemniaki 1.2
      pomidory 4.5
      marchew 0.5
2. Wyświetlam słownik
3. Pytam użytkownika o produkt i sprawadzam czy jest w produktach
4. Wczytujemy ile kg uzytkownik chce kupic
5. Liczymy należnosc
"""

# produkty = {
#     'ziemniaki': 1.2,
#     'pomidory': 4.5,
#     'marchew': 0.5,
# }
# print('Lista produktów:')
# for produkt, cena in produkty.items():
#     print(f'{produkt} - {cena:.2f} zł/kg')
# produkt = input('podaj nazwę produktu')
# if produkt not in produkty:
#     print('brak takiego towaru')
#     exit()
# cena = float(input('podaj ilość w kilogramach:'))
# kwota = produkty[produkt] * cena
# print(f'za {cena} kg produktu {produkt} zapłacisz {kwota} PLN')

print("_" * 65, "zadanie ze słowników2 ")

"""
Napisz program zliczający liczbę wystąpień każdego znaku
w podanym przez użytkownika napisie.


1. Robimy pusty słownik, w którym będziemy zliczać litery
2. Wczytujemy napis od użytkownika
3. Przechodzimy przez wszystkie znaki (for)
  3a. jesli nie ma danego znaku w slowniku to dodajemy
  4b. jezeli jest to zwiększamy liczbe o 1


slownik
klucz  => wartość
litera => liczba wystąpień (int)

Trzeba sprawdzić czy dana litera wystepuje w slowniku!
"""

# tekst = input('podaj dowolny tekst')
# wystapienie = {}
# for litera in tekst.lower():
#     if litera not in wystapienie:
#         wystapienie[litera] = 1
#     else:
#         wystapienie[litera]+=1
# print(wystapienie)

print("_" * 65, "zbiory")

# zbiór nie jest uprządkowany i nie pozwala na wprowadzanie duplikatów

# zbior = {10,10,10,20,30,52,10,85}
# i = 1
# while i < 10:
#     a = input('podaj liczbę')
#     zbior.add(a)
#     i += 1
# for element in zbior:
#     print(element)


# a = {1,2,3,4}
# b = {1,2,3,5}

# suma dwóch zbiorów (łączenie)
# print(a.union(b))
# print(a|b) # operator pipe robi dokładnie to samo

# cześć wspólna dwóch zbiorów lub przecięcie dwóch zbiorów
# print(a.intersection(b))
# print(a&b) # operator & robi dokładnie to samo

# różnica dwóch zbiorów
# print(a.difference(b))
# print(a-b)
#
# # różnica symetryczna
# print(a.symmetric_difference(b))
# print(a^b)
#
# # czy zbiory sa rołączne  - brak częśći wspólnej
# print(a.isdisjoint(b))
# print(not bool(a&b))

# print(a <= b) # sprawdzenie czy a jest podzbiorem b
# print(a >= b) # sprawdzenie czy a jest podzbiorem b
# print(a == b) # sprawdzenie czy a jest podzbiorem b


"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
Sprawdź jak dużo z tych liczb jest liczbami parzystymi
w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu.





1 czesc - ile unikalnych liczb uzytkownik wprowadzil
w petli (while) wczytujemy dane do zbioru, koniec przerywa petle
po petli pokazujemy ile unikalnych liczb zostalo wczytanych i jakie to byly

2 czesc - ile wprowadzonych liczb bylo parzystych w zakresie od 0 do 100
trzeba sobie zrobic zbior liczb parzystych - mozna uzyc petli for i funkcji range(0, 101, 2)
robimy iloczyn teoriomnogosciowy na dwoch zbiorach, zeby pokazac ktore wprowadzone, byly parzyste
"""

# i=0
# zbior_parzyste = set()
# zbior_nieparzyste = set()
# while i >= 0:
#     liczba = float(input('podaj dowolną liczbę w zakresie od 1 do 100. jesli nie chcesz pokawać kolejnych wpisz 000: '))
#     if liczba == 000:
#         break
#     elif liczba % 2 == 0:
#         zbior_parzyste.add(liczba)
#         i = i +1
#     elif liczba % 2 != 0:
#         zbior_nieparzyste.add(liczba)
#         i= i+1
# print(f'ilość wprowadzonych liczb parzystych{len(zbior_parzyste)}')
# print(f'ilość wprowadzonych liczb nieparzytych {len(zbior_nieparzyste)}')
# print(f'ilość wszystkich liczb {len(zbior_parzyste|zbior_nieparzyste)}')
# print(i)

# print("_" * 65, "list comprehension")
# # comprehensions (wyrażaniea )mają 3 rodzaje
# # (list - listowe )
#
# # takie same wyrażenia na 2 sposoby
# # wynik = []
# # for liczba in range(0,11):
# #     wynik.append(liczba)
# # print(wynik)
# #
# # wynik = [liczba*2 for liczba in range(0,11)]
# # print(wynik)
# #
# # # takie same wyrażenia na 2 sposoby
# #
# # wynik = []
# # for liczba in range(0,11):
# #     if liczba %2==0:
# #         wynik.append(liczba *2 )
# #     else:
# #         wynik.append(liczba)
# # print(wynik)
# #
# wynik = [liczba*2 if liczba %2 ==0 else liczba for liczba in range(0,11)]
# print(wynik)
#
#
# print("_" * 65, "set comprehension")
#
#
# literki = {litera for litera in "Ala ma kota"}
# print(literki)
# print(type(literki))


print("_" * 65, "dict comprehension")

# napis = "Ala ma kota"
# wystapienia = {litera: napis.count(litera) for litera in napis}
# print(wystapienia)

#funkcja zip łączy dwie listy

# imiona = ['piotr','kamil', 'asia']
# wynagrodzenie = [10,20,30,40]
# wynik_zip = zip(imiona,wynagrodzenie)
# wynik_zip= list(wynik_zip)
# print(wynik_zip)


print("_" * 65, "generator expression")
# #
# liczby = (liczba for liczba in range(1,11))
# print(liczby)
# for x in liczby:
#     print(x)


print("_" * 65, "praca domowa")
"""
Stwórz następujące struktury danych korzystając ze skróconej wersji zapisu:
- (a) listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
- (b) zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian - w przedziale od -10 do 10
{(-8, 64, -512), (-1, 1, -1), (9, 81, 729), (4, 16, 64), (5, 25, 125), (2, 4, 8), (-9, 81, -729), (3, 9, 27), (-6, 36, -216), (7, 49, 343), (-4, 16, -64), (0, 0, 0), (-7, 49, -343), (10, 100, 1000), (-5, 25, -125), (-2, 4, -8), (8, 64, 512), (-10, 100, -1000), (-3, 9, -27), (6, 36, 216), (1, 1, 1)}
- (c) słownik mapujący napisy na ich długość powstały ze zbioru napisów
{
    'a': 1,
    'Tom': 3,
    'Amy': 3,
    'To be or not to be': 18
}
"""
print("_" * 65, "zad cz 1 pierwszy sposób")
# zad cz 1 pierwszy sposób
# wynik = [liczba/10 for liczba in range(1,11)]
# print(wynik)

# zad cz 1 drugi sposób
# a= []
# for liczba in range(1,10):
#     a.append(liczba/10)
# print(a)

print("_" * 65, "zad cz 2 pierwszy sposób")
# zad cz 2 pierwszy sposób
# b = {(liczba,liczba **2,liczba **3)for liczba in range(-10,11)}
# print(b)


print("_" * 65, "zad cz 2 pierwszy sposób")
# dane = {'a', 'Tom', 'Amy', 'To be or not to be'}
# c = {napis: len(napis) for napis in dane}
# print(c)

# zadanie cz3 drugi sposób
# dane = {'a', 'Tom', 'Amy', 'To be or not to be'}
# d = {}
# for napis in dane:
#    d[napis] = len(napis)
# print(d)

# napis = input('podaj napis:')
# dane = napis.split(' ')
# print(dane)
# dlugosc = {napis: len(napis) for napis in dane}
# print(dlugosc)











