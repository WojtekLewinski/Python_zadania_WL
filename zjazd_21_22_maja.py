"""(Pominięte zadanie na zajęciach)
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego. Klasa powinna umożliwiać pokonanie
zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. Samochód powinien
mieć także możliwość naładowania baterii.
# >>> car = ElectricCar(100)
# >>> car.drive(70)
# 70
# >>> car.drive(50)
# 30
# >>> car.drive(50)
# 0
# >>> car.charge()
# >>> car.drive(50)
50"""

class electricCar:
    def __init__(self,dystans):
        self.dystans = dystans
        self.przebyte = 0
        self.laduje = 0


    def naladuj(self,ladowanie):
        self.laduje = ladowanie
        if self.laduje < self.przebyte:
            self.dystans += self.laduje


    def droga(self,odleglosc):
        self.przebyte = self.dystans - odleglosc
        if odleglosc < 0:
            print(f'jedziesz na wstecznym ')
        elif odleglosc == 0:
            print(f'nadal stoisz ')
        elif odleglosc < self.dystans:
           self.dystans -= odleglosc
        else:
            print(f'samochód tyle nie przejedzie')



    def wypisz(self):
        print(f'samochód może przejechać jeszce {self.dystans}')

a = electricCar(100)
a.wypisz()
a.droga(20)
a.wypisz()
a.naladuj(1)
a.naladuj(22)
a.wypisz()

print('_'*40,'nowe zadanie  klasa dom')
print('_'*40,'dziedziczenie')
#
#
# class Employee:
#     def __init__(self, imie, nazwisko, pensja):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.pensja = pensja
#         self.przepracowane_godziny = 0
#
#     def register_time(self, h):
#         if h <= 8:
#             self.przepracowane_godziny += h
#         else:
#             self.przepracowane_godziny += 8 + (h - 8) * 2
#
#     def pay_salary(self):
#         wynagrodzenie = self.przepracowane_godziny * self.pensja
#         self.przepracowane_godziny = 0
#         return wynagrodzenie


# Zaimplementuj klasę PremiumEmployee, która będzie klasą
# pochodną Employee. Klasa ta powinna umożliwiać dodatkowo
# przyznawanie bonusów pracownikowi.
# >>> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.give_bonus(1000.0)
# >>> employee.pay_salary()
# 1500.0

# class PremiumEmployee(Employee):
#     def __init__(self, imie, nazwisko, pensja):
#         super().__init__(imie, nazwisko, pensja)
#         self.bonus = 0
#
#
#     def pay_salary(self):
#         w = super().pay_salary() + self.bonus
#         self.bonus = 0
#         return w
#
#     def dodatek(self,kwota):
#         self.bonus += kwota
#
#
# a = PremiumEmployee("Jan","Nowak",100)
# a.register_time(8)
# a.bonus = 1000
# print(a.pay_salary())


print('_'*40,'wyjątki')
#
# def niebezpieczna_funkcja(x):
#     if x == 0:
#         raise ValueError("Nie wpisuj zera")
#     return 2*x+3
# x= niebezpieczna_funkcja(0)
# print(x)

# Napisz funkcję przyjmij_int(), ktora będzie prosić użytkownika o podanie liczby całkowitej tak długa, aż nie zostanie takowa
# podana. Skorzystaj z mechanizmu wyjątków.

# def przyjmij_int():
#     while True:
#         try:
#             x = int(input(f'Podaj dowolną liczbę całkowitą:'))
#             return x
#         except ValueError:
#             print("Podales cos co nie jest intem")

print('_'*40,'iteratory')

# class Licznik:
#     def __init__(self, limit):
#         self.limit = limit
#
#     # __iter__() musi zwrocic iterator (obiekt posiadający metodę __next__())
#     def __iter__(self):
#         print("__iter__()")
#         self.nastepna = 0
#         return self
#
#     def __next__(self):
#         print("__next__()")
#         if self.nastepna >= self.limit:
#             raise StopIteration
#         wynik = self.nastepna
#         self.nastepna += 1
#         return wynik
#
#
# licznik = Licznik(5)
# for x in licznik:
#     print(x)




# Zaimplementuj iterator zwracający jedynie samogłoski z zadanego
# ciągu znaków:
# Przykładowe użycie:
# for char in Samogloski("Ala ma kota"):
#     print(char)
# Wynik:
#     A
#     a
#     a
#     o
#     a

# class samogloski():
#     def __init__(self, napis):
#         self.napis = napis
#         self.lista = ["a","i","e","o","u"]
#
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         while self.index < len(self.napis):
#             litera = self.napis[self.index]
#             self.index +=1
#             if litera.lower() in "aeoiu":
#                 return litera
#         raise StopIteration
#
# for znak in samogloski("Ala ma kota a kot ma Ale"):
#     print(znak)
#
#
# napis = samogloski("Ala ma kota a kot ma Ale")
#
#
print('_'*40,'generatory')
#
# def samogloski2(napis):
#     for litera in napis:
#         if litera.lower() in "aeoiu":
#             yield litera
#
#
# for x in samogloski2("Ala ma kota"):
#     print(x)
#     print("Znalazlem samogloske", x)
#
# print(list(samogloski2("mnkajlvnkajdsnvkjavnkjabjv hbJHBdJHbj")))

print('_'*40,'praca z plikami')

# Napisz program wypisujący na konsolę zawartość wskazanego pliku
# wraz z numerami linii. Obsłuż sytuację, gdy użytkownik nie poda
# nazwy pliku lub poda błędną nazwę.
# Przykład użycia:
# $ python test.txt
# 1: pierwsza linia pliku
# 2: druga linia pliku

# plik = open("test.txt.py")
# print(plik)
# print(plik.read())
# plik.seek(4)
# # plik.seek(-3, 1) # cofamy kursor o 3 pozycje
# print(plik.read())
# plik.close()

# plik otwarty w bloku `with` zostanie automatycznie zamknięty

# poprawna_nazwa_pliku = "test.txt.py"
# nazwa = input("Podaj nazwę pliku:")
# if nazwa != poprawna_nazwa_pliku:
#     print("Wpisałeś błędną nazwę")
# else:
#     with open(nazwa) as otwarty_plik:
#         tresc = otwarty_plik.read()
#
# wiersze = tresc.split('\n')
# for a in range(len(wiersze)):
#     print(a,wiersze[a])


"""Napisz program wczytujący listę adresów email z pliku i tworzący
nowy plik z odfiltrowaną zawartością.
Wejściowy plik może zawierać duplikaty adresów, ten sam adres
pisany różną wielkością liter, linie zawierające białe znaki oraz
błędne adresy email (brak znaku @ lub występuje on wiele razy).
Wynikowy plik powinien zawierać unikalne, posortowane, poprawne
adresy email."""

# with open("test") as otwarty_plik:
#     tresc = otwarty_plik.read().lower().replace(" ","")
#
# zbior = []
# wiersze = tresc.split('\n')
# for a in range(len(wiersze)):
#     if wiersze[a].count('@') == 1:
#         zbior.append(wiersze)
# print(wiersze)

print('_'*40,'moduł json')
import json



"""Napisz program obsługujący bazę danych pracowników. W bazie
danych przechowuj imię, nazwisko, email, rok urodzenia, pensję.
Skorzystaj z modułu json.
Przykład użycia:
$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] d
Imie: Jan
Nazwisko: Nowak
Rok urodzenia: 1980
Pensja: 5000.0
$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] w
Pracownicy:
- [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN"""



# try:
#     with open("pracownicy.json") as plik:
#         lista = json.load(plik)
# except FileNotFoundError:
#     lista = []
# a = input("Czcesz dodać: 'D', czy wypisać użytkowników: 'W':")
# if a == "D":
#     slownik = {}
#     slownik["Imie"] = input("Podaj imie:")
#     slownik["Nazwisko"] = input("Podaj nazwisko:")
#     slownik["Rok urodzenia"] = input("Podaj rok urodzenia:")
#     slownik["Pensja"] = input("Podaj pensję:")
#     lista.append(slownik)
#     with open("pracownicy.json","w") as plik:
#         json.dump(lista,plik,indent=1)
# else:
#     print(lista)

print('_'*40,'moduł urlopen')

from urllib.request import urlopen
import json

#
# with urlopen("http://api.nbp.pl/api/cenyzlota?format=json") as plik:
#     lista = json.load(plik)
# print("Aktualna cena złota:", lista[0]['cena'])

# with urlopen("http://api.nbp.pl/api/cenyzlota?format=json") as plik:
#     lista = json.load(plik)
# print("Aktualna cena złota:", lista[0]['cena'])

from urllib.request import urlopen, Request
import json

# with urlopen("https://www.kindpng.com/picc/m/5-51409_meme-sad-frog-clipart-sad-frog-hd-png.png") as plik:
#     tresc = plik.read()
#
# print(type(tresc))
# # print(tresc)
# with open("zaba.png", 'wb') as plik:
#     plik.write(tresc)
topCount = 10


# with urlopen("http://api.nbp.pl/api/cenyzlota?format=json") as plik:
#     lista = json.load(plik)
# print("Aktualna cena złota:", lista[0]['cena'])

# h = {"User-Agent": "Chrome"}
# zapytanie = Request("https://api.chucknorris.io/jokes/categories", headers=h)
# with urlopen(zapytanie) as plik:
#     kategorie = json.load(plik)
#     print(f'kategorie to:{" ".join(kategorie)}')
# a = input("Wpisz  kategorię:")
# zapytanie = Request(f'https://api.chucknorris.io/jokes/random?category={a}', headers=h)
# with urlopen(zapytanie) as plik:
#     zart = json.load(plik)
# print(zart["value"])


print('_'*40,'moduł tkinter')
# def fun():
#     print(("Przycisk został naciśnięty."))
#     tresc = pole_tekstowe.get()
#     print(f'Treść pola: {tresc}')
#     tekst.configure(text = tresc)
#
# import tkinter as tk
# root = tk.Tk()
# przycisk = tk.Button(master=root, text="Click me!", command=fun)
# przycisk.grid(row = 0, column =0)
#
# pole_tekstowe = tk.Entry(master=root)
# pole_tekstowe.grid(row = 1, column = 1)
#
# tekst = tk.Label(master=root, text = "To jest Label")
# tekst.grid(row=0, column =1)
#
# root.mainloop()

import tkinter as pole

root = pole.Tk() #od tego zaczynamy i to zawsze jest w takiej postaci
root.title("Nowa nazwa")
def oblicz():
    tresc1 = float(dystans.get())
    tresc2 = float(spalanie.get())
    tresc3 = float(cena.get())
    print(f'Treść pola: {tresc1*tresc2*tresc3/100}')



przycisk = pole.Button(master=root, text="Wylicz!", command=oblicz)
przycisk.grid(row = 3, column = 0)
dystans = pole.Entry(master=root)
dystans.grid(row = 0, column = 1)
spalanie = pole.Entry(master=root)
spalanie.grid(row = 1, column = 1)
cena = pole.Entry(master=root)
cena.grid(row = 2, column = 1)

tekst = pole.Label(master=root, text = "Dystans")
tekst.grid(row=0, column =0)
tekst2 = pole.Label(master=root, text = "Spalanie")
tekst2.grid(row=1, column =0)
tekst3 = pole.Label(master=root, text = "Cena Paliwa")
tekst3.grid(row=2, column =0)

root.mainloop()

sticky = pole.E