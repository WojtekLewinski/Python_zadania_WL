"""
Zadanie 2.1 | Zagadka matematyczna
Program losuje dwie liczby z zakresu od 0 do 99. Podaje te dwie liczby i pyta jaka jest ich
suma (nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta
o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
"""


import random
liczba1 = random.randint(0, 99)
liczba2 = random.randint(0, 99)
suma = int(input(f'Jaka jest suma {liczba1} i {liczba2}?'))
while suma != liczba1 + liczba2:
    print(f'Podana przez Ciebie liczba jest błędna. Sprubuj jeszcze raz!')
    suma= int(input(f'Kolejna próba:'))
print("Trafiłeś")


