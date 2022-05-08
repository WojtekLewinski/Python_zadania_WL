print(f'____' * 25, "Zadanie 1")
""" napisz funkcję wykonującą silnię """

# def silnia(liczba: int)->int:
#     wynik = 1
#     for i in range(1, liczba + 1):
#         wynik *= i
#     return wynik
#
#
# print(f'{silnia(5) = }')

print(f'____' * 25, "funkcja rekurencyjna - zainteresuj się językami funkcyjnymi")

# 0! = 1
# n! = n *(n-1)!

# def silnia_rekurencyjna(n: int) -> int:
#     if n == 0:
#         return 1
#     return n * silnia_rekurencyjna(n-1)
#
# print(f'{silnia_rekurencyjna(5) = }')

print(f'____' * 25, "Zadanie 2")

"""liczby fibonnaciego"""
# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2)

# def ciag_f(n: int) ->int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return ciag_f(n - 1) + ciag_f(n-2)
#
# print(f'{ciag_f(9)}')
"""dokończ w domu bo jest źle_"""
# def fib(liczba: int) ->int:
#     wynik1 = 1
#     zmi_1 = 0
#     zmi_2 = 0
#     for a in range(1,liczba):
#         zmi_2 = wynik1 + zmi_1
#         zmi_1 = zmi_2 + wynik1
#         wynik1 = zmi_1
#     return wynik1
# #
# print(f'{fib(3)}')


print(f'____' * 25, "Zadanie 3")

"""funkcja spłaszczajaca listę"""

# def splaszcz(lista):
#     lista_wynikowa=[]
#     for a in lista:
#         print(a, type(a))
#         if isinstance(a, list):
#             for x in splaszcz(a):#wykorzystaliśmy tu rekurencję. Funkcja odwołuje sioesama do siebie
#                 lista_wynikowa.append(x)
#         else:
#             lista_wynikowa.append(a)
#     return lista_wynikowa
#
#
#
# print(splaszcz([1,2,[3,[[[[4]],5]]],5]))

print(f'____' * 25, " nowy temat")

"""napisz funkcje zaaplikój która przyjmie funkcje f oraz liste wartośći  a następnie zwrócu listę wyników fdla wszystkich wartosći """

# Napisz funkcję `zaaplikuj`, ktora przyjmie funkcję `f` oraz listę wartości, a następnie
# zwróci listę wyników funkcji `f` dla wszystkich wartości z listy
# zaaplikuj(f, [a,b,c]) == [f(a), f(b), f(c)]

# def zaaplikuj(fun, lista):
#     wynik = []
#     for a in lista:
#         wynik.append(funkcja(a))
#     return wynik
#
# def funkcja(x):
#     return 'f',(x)
#
# print(zaaplikuj(funkcja, [10, 21, 30]))
#
#
#
# def zaaplikuj1(funk1,lista1):
#     wartosc = []
#     for c in lista1:
#         wartosc.append(dodawanie(c))
#     return wartosc
#
#
# def dodawanie(z):
#     return z + 10
#
# print(zaaplikuj1(dodawanie,[1,2,3]))


# def kwadrat(x):
#     return x ** 2
#
# def test_zaaplikuj():
#     assert zaaplikuj(kwadrat, [1, 2, 3, 4]) == [1, 4, 9, 16]


# lista = [1,2,3,4,5]
# def kwadrat(x):
#     return x ** 2
#
# print(list(map(kwadrat,lista)))

print(f'____' * 25, " funkcje anonimowe")

# lista = [1,2,3,4,5]
#
# def kwadrat(x):
#     return x ** 2
#
# print(map(kwadrat, lista))
# print(list(map(kwadrat, lista)))
#
# print(list(map(lambda x: x + 7, lista)))
# print(list(map(lambda x: x ** 3, lista)))
#
# plus5 = lambda x: x + 5
#
# print(list(filter(lambda x: x % 2 == 0, lista)))

# (lambda x, y: print(f"{x + y = }"))(5, 10) # od razu wywołuję funkcję anonimową


# przykład
# Przyjmij od użytkownika listę intów rozdzieloną przecinkami i zamień
# przyjęty napis na listę intów
# Haczyk: limit wierzy == 1
# "1,2,3,4,5" -> [1,2,3,4,5]

# wersja w kilku wierszach
# napis = input('podaj napis:')
# dane = napis.split(',')
# int = []
# for s in dane:
#     int.append(s)
# print(int)
#
# # wersja w jednym wierszu
# print(list(map(int, input('podaj napis:').split(',')))) # w tym przypadku funkcja map przypisuje wszystkim elementom listy wartość int


print(f'____' * 25, " programowanie obiektowe")

# class Moja_klasa:
#     def metoda(self,x):
#         print(f'wywołano metodę z argumentem {x}' )
#
# x = Moja_klasa()# tworzy nowy obiekt typu Moja Klasa
# print(x)
# print(type(x))
# x.metoda(10)

# class Osoba:
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def przedstaw_sie(self):
#         print(f'Cześć!Jestem  {self.imię} {self.nazwisko}')
#
# jan = Osoba("Jan", "Kowalski")
#
# print(f'____'*25," Zadanie 1 klasy")
#
# class Produkt:
#     def __init__(self,waga, cena, id):
#         self.waga = waga
#         self.cena = cena
#         self.id = id
#
#     def wypisz_informacje(self):
#         print(f'ID produktu:{self.id}, Waga w kilogramach:{self.waga}, Cena w PLN:{self.cena}')
#
#
#
# kawa = Produkt(1,5,33)
# mleko = Produkt(1,4,7)
# kawa.wypisz_informacje()
# print(kawa.id)


print(f'____' * 25, " Zadanie 2")

# class Pracownik:
#     def __init__(self, imie, nazwisko, stawka,):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.stawka = stawka
#         self.czas_pracy = 0
#
#     def czas_pr(self, h):
#         if h <= 8:
#             self.czas_pracy += h
#         else:
#             self.czas_pracy += 8 + (h - 8 ) * 2
#
#     def wyplata(self):
#         wynagrodzenie = self.czas_pracy*self.stawka
#         self.czas_pracy = 0
#         return wynagrodzenie
##
# jan = Pracownik("Jan","Kowalski", 100)
# jan.czas_pr(5)
# jan.czas_pr(9)
# print(jan.wyplata())
#
#
# def test_0():
#     e = Pracownik("Jan", "Kowalski", 100)
#     e.czas_pr(5)
#     assert e.wyplata() == 500
#     assert e.wyplata() == 0
#     e.czas_pr(5)
#     e.czas_pr(5)
#     assert e.wyplata() == 1000
#     e.czas_pr(10)
#     assert e.wyplata() == 1200

print(f'____' * 25, " Zadanie 2 _klaca postaci")

#
# class Postac:
#     def __init__(self, imie, zdrowie):
#         self.imie = imie
#         self.zdrowie = zdrowie
#         self.leczenie = 0
#         self.rany = 0
#
#     def wypisz(self):
#         print(f'Bohater {self.imie} ma {(self.zdrowie - self.rany) + self.leczenie} pkt zdrowia')
#
#     # zmniejsza zdrowie o dmg; zdrowie nie powinno spaść poniżej 0
#     def otrzymaj_obrazenia(self, dmg):
#         if self.zdrowie - dmg >= 0 and self.zdrowie - dmg > 0:
#             print(f'Bohater otrzymał {dmg} pkt obrażeń')
#             self.rany += dmg
#             self.zdrowie - self.rany
#         else:
#             print("Bohater nie żyje")
#
#             # przywraca `hp` utraconych punktów zdrowia;
#             # zdrowie nie powinno przekroczyć maksymalnej wartosci
#             # leczenie nie działa jesli postac nie zyje
#
#     def wylecz(self, hp):
#         if self.zdrowie > 0 or self.zdrowie + hp <= 120:
#             if (self.zdrowie + hp) > 120:
#                 print(f'Bohater dostał {hp} ma teraz 120 pkt zdrowia')
#                 self.zdrowie = 120
#             else:
#                 print(f'Bohater otrzymał {hp} pkt zdrowia ma teraz {self.zdrowie} pkt zdrowia')
#         else:
#             print(self.zdrowie)
#
#     # zwraca iformację, czy postać żyje
#     def czy_zyje(self):
#         if self.zdrowie > 0:
#             print("Bohater żyje")
#         else:
#             print("Bohater nie żyje")
#
#
# Gunnar = Postac("Gunnar", 120)
# Gunnar.wypisz()  # Rufus, 120/120 HP
# Gunnar.otrzymaj_obrazenia(15)
# Gunnar.wypisz()  # Rufus, 105/120 HP
# Gunnar.wylecz(2)
# Gunnar.wypisz()  # Rufus, 108/120 HP
# Gunnar.wylecz(7)
# Gunnar.wypisz()  # Rufus, 120/120 HP
# Gunnar.otrzymaj_obrazenia(150)
# Gunnar.wypisz()  # Rufus, 0/120 HP / Rufus, nie żyje
#
# p = Postac("Worek treningowy", 100)
# while p.czy_zyje():
#     p.otrzymaj_obrazenia(7)
#     p.wypisz()

print(f'____' * 25, "  klaca produkt")


# Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w
# określonej liczbie do koszyka. Zaimplementuj metodę obliczającą
# całkowitą wartość koszyka oraz wypisującą informację o zawartości
# koszyka. Dodanie dwa razy tego samego produktu do koszyka
# powinno stworzyć tylko jedną pozycję.
# Przykład użycia:
# >>> basket = Basket()
# >>> product = Product(1, 'Woda', 10.00)
# >>> basket.add_product(product, 5)
# >>> basket.count_total_price()
# 50.0
# >>> basket.generate_report()
# 'Produkty w koszyku:\n
# - Woda (1), cena: 10.00 x 5\n
# W sumie: 50.00'

class Produkt:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

class NieProdukt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Koszyk:
    def __init__(self):
        self.zawartosc = []

    def dodaj_produkt(self, p: Produkt, ile=1):
        if not isinstance(p, Produkt):
            print("Do koszyka można wkładać tylko Produkty!")
            return
        self.zawartosc.append({"produkt": p, "ilosc": ile})


    def laczna_wartosc(self):
        suma = 0
        for prod in self.zawartosc:
            suma += prod["produkt"].cena*prod["ilosc"]
        return suma

    def rachunek(self):
        print("Produkty w koszyku:")
        for p in self.zawartosc:
            print(f" - {p.nazwa}, {p.cena}")
        print(f"Suma: {self.laczna_wartosc()} PLN")

woda = Produkt(1, "Woda", 10)
banan = Produkt(2, "Banan", 2)
niewoda = NieProdukt("Woda", 20)
k = Koszyk()
k.dodaj_produkt(woda)
k.dodaj_produkt(banan)
# k.dodaj_produkt(niewoda)
print(k.laczna_wartosc())


def test_0():
    woda = Produkt(1, "Woda", 10.50)
    bulka = Produkt(2, "Bułka", 1.75)
    koszyk = Koszyk()
    koszyk.dodaj_produkt(woda)
    koszyk.dodaj_produkt(bulka)
    assert koszyk.laczna_wartosc() == 12.25

def test_1():
    woda = Produkt(1, "Woda", 10)
    bulka = Produkt(2, "Bułka", 1)
    koszyk = Koszyk()
    koszyk.dodaj_produkt(woda, 3)
    koszyk.dodaj_produkt(bulka, 2)
    assert koszyk.laczna_wartosc() == 32


# if __name__ == "__main__":
woda = Produkt(1, "Woda", 10.50)
bulka = Produkt(2, "Bułka", 1.75)
koszyk = Koszyk()
koszyk.dodaj_produkt(woda, 24)
koszyk.dodaj_produkt(bulka)
koszyk.rachunek()