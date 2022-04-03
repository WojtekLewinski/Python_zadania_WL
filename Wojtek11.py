"""
Zadanie 2.2 | Choinka
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu
liniach "choinkę" ze znaków * . Np. dla parametru 3 powinno się wypisać:
"""

poziomy = int(input(f'Podaj dodatnią liczbę całkowitą:'))
pierwszy = 1
for a in range(0,poziomy):
    print(" " * poziomy + "*" * pierwszy)
    poziomy=poziomy-1
    pierwszy = pierwszy + 2
    1



