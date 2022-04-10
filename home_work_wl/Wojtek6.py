"""Zadanie 1.6 | Bilety (ok. 1 godz.)

Założenia: -
0-6 - wiek przedszkolny - cena biletu: 0
7-17 - wiek szkolny - cena biletu: 2.28
18-64 - wiek dorosły - cena biletu: 3.80
+65 - wiek emerytalny - cena biletu: 1.90
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile
biletów chce kupić.
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli"""

wiek = int(input("Podaj wiek"))
bilety = int(input("Ile biletów chcesz kupić"))
if wiek <= 6:
    print("Darmowe wejście")
elif wiek > 6 and wiek <= 17:
    print(f'Bilet kosztuje {bilety * 2.38} PLN')
elif wiek > 17 and wiek <= 64:
    print(f'Bilet kosztuje {bilety * 3.80} PLN')
else:
    print(f'Bilet kosztuje {bilety * 1.90} PLN')
