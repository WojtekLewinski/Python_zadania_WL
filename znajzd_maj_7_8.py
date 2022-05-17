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
#         print(f'Cześć!Jestem  {self.imie} {self.nazwisko}')
#
#
# jan = Osoba("Jan", "Kowalski")
# jan.przedstaw_sie()



#
print(f'____'*25," Zadanie 1 klasy")

class Produkt:
    def __init__(self,waga, cena, id):
        self.waga = waga
        self.cena = cena
        self.id = id

    def wypisz_informacje(self):
        print(f'ID produktu:{self.id}, Waga w kilogramach:{self.waga}, Cena w PLN:{self.cena}')



kawa = Produkt(1,5,33)
mleko = Produkt(1,4,7)
kawa.wypisz_informacje()
print(kawa.id)


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
# #
# jan = Pracownik("Jan","Kowalski", 100)
# jan.czas_pr(5)
# jan.czas_pr(9)
# print(jan.wyplata())


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


class Postac:
    def __init__(self, imie, zdrowie):
        self.imie = imie
        self.zdrowie = zdrowie
        self.leczenie = 0
        self.rany = 0
        self.po_obrażeniach = self.zdrowie - self.rany

    def wypisz(self):
        print(f'Bohater {self.imie} ma {(self.zdrowie - self.rany) + self.leczenie} pkt zdrowia')

    # zmniejsza zdrowie o dmg; zdrowie nie powinno spaść poniżej 0
    def otrzymaj_obrazenia(self, dmg):
        if self.zdrowie - dmg >= 0 and self.zdrowie - dmg > 0:
            print(f'Bohater otrzymał {dmg} pkt obrażeń')
            self.rany += dmg
            self.zdrowie - self.rany
        else:
            print("Bohater nie żyje")

            # przywraca `hp` utraconych punktów zdrowia;
            # zdrowie nie powinno przekroczyć maksymalnej wartosci
            # leczenie nie działa jesli postac nie zyje

    def wylecz(self, hp):
        if self.zdrowie > 0 or self.zdrowie <= 120:
            if (self.po_obrażeniach + hp) > 120:
                print(f'Bohater dostał {hp} pkt zdrowia ma {self.po_obrażeniach}')
            else:
                print(f'Bohater otrzymał {hp} pkt zdrowia ma teraz {self.zdrowie + hp} pkt zdrowia')
        else:
            print(self.zdrowie)

    # zwraca iformację, czy postać żyje
    def czy_zyje(self):
        if self.zdrowie > 0:
            print("Bohater żyje")
        else:
            print("Bohater nie żyje")


Gunnar = Postac("Gunnar", 120)
Gunnar.wypisz()  # Rufus, 120/120 HP
Gunnar.otrzymaj_obrazenia(15)
Gunnar.wypisz()  # Rufus, 105/120 HP
Gunnar.wylecz(2)
Gunnar.wypisz()  # Rufus, 108/120 HP
Gunnar.wylecz(7)
Gunnar.wypisz()  # Rufus, 120/120 HP
Gunnar.otrzymaj_obrazenia(150)
Gunnar.wypisz()  # Rufus, 0/120 HP / Rufus, nie żyje

p = Postac("Worek treningowy", 100)
while p.czy_zyje():
    p.otrzymaj_obrazenia(7)
    p.wypisz()

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

# class Produkt:
#     def __init__(self, id, nazwa, cena):
#         self.id = id
#         self.nazwa = nazwa
#         self.cena = cena
#
# class NieProdukt:
#     def __init__(self, nazwa, cena):
#         self.nazwa = nazwa
#         self.cena = cena
#
# class Koszyk:
#     def __init__(self):
#         self.zawartosc = []
#
#     def dodaj_produkt(self, p: Produkt, ile=1):
#         if not isinstance(p, Produkt):
#             print("Do koszyka można wkładać tylko Produkty!")
#             return
#         self.zawartosc.append({"produkt": p, "ilosc": ile})
#
#
#     def laczna_wartosc(self):
#         suma = 0
#         for prod in self.zawartosc:
#             suma += prod["produkt"].cena*prod["ilosc"]
#         return suma
#
#     def rachunek(self):
#         print("Produkty w koszyku:")
#         for p in self.zawartosc:
#             print(f" - {p.nazwa}, {p.cena}")
#         print(f"Suma: {self.laczna_wartosc()} PLN")
#
# woda = Produkt(1, "Woda", 10)
# banan = Produkt(2, "Banan", 2)
# niewoda = NieProdukt("Woda", 20)
# k = Koszyk()
# k.dodaj_produkt(woda)
# k.dodaj_produkt(banan)
# # k.dodaj_produkt(niewoda)
# print(k.laczna_wartosc())
#
#
# def test_0():
#     woda = Produkt(1, "Woda", 10.50)
#     bulka = Produkt(2, "Bułka", 1.75)
#     koszyk = Koszyk()
#     koszyk.dodaj_produkt(woda)
#     koszyk.dodaj_produkt(bulka)
#     assert koszyk.laczna_wartosc() == 12.25
#
# def test_1():
#     woda = Produkt(1, "Woda", 10)
#     bulka = Produkt(2, "Bułka", 1)
#     koszyk = Koszyk()
#     koszyk.dodaj_produkt(woda, 3)
#     koszyk.dodaj_produkt(bulka, 2)
#     assert koszyk.laczna_wartosc() == 32
#
#
# # if __name__ == "__main__":
# woda = Produkt(1, "Woda", 10.50)
# bulka = Produkt(2, "Bułka", 1.75)
# koszyk = Koszyk()
# koszyk.dodaj_produkt(woda, 24)
# koszyk.dodaj_produkt(bulka)
# koszyk.rachunek()

print(f'____' * 25, "  magiczne moteody")


# np __init__

# class Produkt:
#     def __init__(self, nazwa, cena):
#         self.nazwa = nazwa
#         self.cena = cena
#
#     def __str__(self):
#         return f'{self.nazwa}, cena: {self.cena} PLN'
#
#
# p = Produkt("Woda", 12)
# print((p.__str__()))
# print(p)

print(f'____' * 25, "  klasa ułamek")


class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __imul__(self, other):  # a.domnoz(b) - a *= b
        self.licznik *= other.licznik
        self.mianownik *= other.mianownik
        return self

    def __mul__(self, other):
        return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def dodaj(self, other):  # a.dodaj(b) - a += b
        self.licznik = self.licznik * other.mianownik + self.mianownik * other.licznik
        self.mianownik *= other.mianownik


a = Ulamek(1, 2)
b = Ulamek(2, 3)
print(a)
c = a * a # to samo co c = a.__mul__(a)
print(a)
print(c)
print(a)  # tu print() wywoła sobie a.__str__(), żeby wiedziec jak ma wyswietlic a
# a.domnoz(b)
a *= b # to samo co a = a.__imul__(b)
print(a)
a.dodaj(b)
print(a)

print(f'____' * 25, "  pola klasowe")

# class MojaKlasa:
#     POLA_KLASOWE = 100
#
#     def __init__(self,x):
#         self.atrybut = x
#
#
# MojaKlasa.POLA_KLASOWE = 200
# print(f'{MojaKlasa.POLA_KLASOWE = }')
# a = MojaKlasa(5)
# b = MojaKlasa(10)
#
#
# print(f'{a.atrybut = }')
# print(f'{b.atrybut = }')
# print(f'{b.POLA_KLASOWE = }')

print(f'____' * 25, "  pola klasowe")

class Produkt2:
    POLE_KLASOWE = 1

    def __init__(self, nazwa_produktu, cena_produktu):
        self.nazwa_produktu = nazwa_produktu
        self.cena_produktu = cena_produktu
        self.nr_produktu = Produkt2.POLE_KLASOWE
        Produkt2.POLE_KLASOWE +=1


    def wyliczenie(self):
        print(f'Produkt: {self.nazwa_produktu}, nr ID:{self.nr_produktu}, cena:{self.cena_produktu}')



banan = Produkt2("Banan",1)
cytryna = Produkt2("cytryna",3)
banan.wyliczenie()
cytryna.wyliczenie()


"""1. (Pominięte zadanie na zajęciach)
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego. Klasa powinna umożliwiać pokonanie
zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. Samochód powinien
mieć także możliwość naładowania baterii.
>>> car = ElectricCar(100)
>>> car.drive(70)
70
>>> car.drive(50)
30
>>> car.drive(50)
0
>>> car.charge()
>>> car.drive(50)
50


2.
	a. Do klasy Postac (z zajęć) dodaj atrybut 'atak' (będący liczbą) ustawiany w konstruktorze oraz metodę daj_atak(), która zwróci wartość ataku Postaci.

	b. Stwórz klasę Przedmiot, który będzie posiadał nazwę i jakiś bonus liczbowy (np. Przedmiot("Kij", 4) => Przedmiot o nazwie "Kij" i bonusie 4) oraz będzie posiadał sensowną reprezentację napisową (metoda __str__()).

	c. Rozszerz klasę Postać o ekwipunek - dodaj metody:
        - daj_przedmiot(p) - dodaje Przedmiot(zad 2b.) do ekwipunku,
        - wypisz_ekwipunek - wypisuje wszystkie Przedmioty posiadane przez daną Postać.

	d. W klasie Postać (zad 2a.) zmodyfikuj metodę daj_atak(), żeby zwracała wartość ataku Postaci powiększoną o sumę bonusów z posiadanych w ekwipunku(zad 2c.) Przedmiotów(zad 2b.).

3. Zmoyfikuj klasę Ulamek (z zajęć) tak, aby:
    - dodawanie i mnożenie można było wykonać nie tylko z innym Ulamkiem, ale też z intem, niezależnie po której stronie działania się znajdzie (tj. powinno działać zarówno `x * 5` jak i `5 * x`)
    - możliwa była zmiana znaku Ulamka (metoda __neg__())
    - możliwe było wykorzystanie operatorów logicznych: <, <=, >, >=, ==, != działających dla porówniań ułamka z ułamkiem, ułamka z intem i inta z ułamkiem.
    - (*) po każdym działaniu na Ulamku był on w postaci nieskracalnej (tzn. 1/4 + 1/4 powinno dać w wyniku ułamek 1/2 a nie 2/4)

4. Wyobraźmy sobie robota, który może poruszać się naprzód i obracać w lewo lub prawo o 90 stopni.
        Napisz klasę Robot, która będzie przechowywała informację o położeniu robota na płaszczyźnie (2 liczby całkowite) oraz
        kierumku w jakim jest zwrócony (N - północ, S - południe, E - wschód, W - zachód).
        Klasa powinna udostępniać metody:
                - wypisz() - wypisuje położenie i zwrot robota,
                - lewo() - zmienia kierunek, w którym zwrócony jest Robot o 90 stopni w kierunku przeciwnym do ruchu wskazówek zegara (np. N zamieniamy na W),
                - prawo() - zmienia kierunek, w którym zwrócony jest Robot o 90 stopni w kierunku zgodnym z ruchem wskazówek zegara (np. N zamieniamy na E),
                - naprzod() - przemieszcza robota krok w kierunku, w którym obecnie jest zwrócony (przykładowo krok na wschód powoduje zmianę współrzędnych z (x, y) na (x + 1, y)),
                - wykonaj(ciag_instrukcji), gdzie ciąg instrukcji to napis złożony z liter N, P, L oznaczających odpowiednio: Naprzód, Prawo, Lewo (tzn. instkcja N odpowiada jednemu wywołaniu metody naprzod(), P - prawo(), L - lewo()).
                        Wywołanie metody wykonaj() powinno przemieścić robota zgodnie z przekazanymi instrukcjami.
                        Przykład:
                        - początkowe położenie robota: (0, 0), zwrot: N,
                        - ciąg instrukcji: NNPNLNPP,
                        - końcowe położenie robota: (1, 3), zwrot: S.

5. (*) Napisz klasę Zolw, która będzie przechowywała informację o położeniu żółwia na płaszczyźnie (2 liczby _rzeczywiste_) oraz kierunku wyrażonym w stopniach, w którym jest zwrócony.
        Zolw powinien udostępniać metody:
                - wypisz() - wypisuje położenie i zwrot żólwia,
                - lewo(n) - obraca żółwia o n stopni w lewo,
                - prawo(n) - obraca żółwia o n stopni w prawo,
                - naprzod(n) - przemieszcza żółwia o n jednostek w kierunku, w którym obecnie jest zwrócony.
        Hint do zadania: `import math` i trygonometria. ;)"""