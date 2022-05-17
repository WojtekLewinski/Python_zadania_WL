""" napisz funkcję wykonującą silnię """

def silnia(liczba: int)->int:
    wynik = 1
    for i in range(1, liczba + 1):
        wynik = i * wynik
    return wynik


print(f'{silnia(5) = }')

def sil(liczba : int):
    wynik = 1
    for i in range(1,liczba):
        wynik *= i
    return wynik

print(f'{silnia(5) = }')