"""
Napisz program, który odczytuje od użytkownika wiele liczb.
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
liczba podanych liczb (ile sztuk),
suma,
średnia,
minimum
maksimum
NIE używaj funkcji wbudowanych!
"""


a = []
while True:
    c = int(input('podaj liczbę'))
    a.append(c)
    d = input('Czy podasz kolejną liczbę T/N')
    if d =='N':
        break
print(f'Liczba podanych przeż użytkownika liczb to: {len(a)}')
print(f'Suma podanych przeż użytkownika liczb to: {sum(a)}')
print(f'Średnia podanych przeż użytkownika liczb to: {sum(a)/len(a)}')
najmniejsza = None
najwieksza = None
for i in a:
    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i
    if najwieksza == None or najwieksza < i:
        najwieksza = i
print(f'Najniższa z podanych przeż użytkownika liczb to: {najmniejsza}')
print(f'Najwyższa z podanych przeż użytkownika liczb to: {najwieksza}')
a
