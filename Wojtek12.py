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
b = int(input('podaj liczbę'))
c = input('Czy chcesz podać kolejną liczbę T/N ?')
a.append(b)
print(f'podane przez ciebie liczby to: {a}')
if c == 'T':
    next(b)




