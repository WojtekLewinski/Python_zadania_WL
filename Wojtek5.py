"""Napisz program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta (np.
z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o
takich bokach.
Wykorzystaj trzeci wzór z listy.
Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek
kwadratowy to:
import math
x = math.sqrt(10)"""

import math

AB = float(input("Podaj długośc pierwszego boku trójkąta"))
BC = float(input("Podaj długośc drugiego boku trójkąta"))
AC =  float(input("Podaj długośc trzeciego boku trójkąta"))
Polowa_obwodu = (AB+BC+AC)/2
pole = math.sqrt(Polowa_obwodu * (Polowa_obwodu - AB) * (Polowa_obwodu - BC) * (Polowa_obwodu - AC))
if AB < (BC + AC) and BC < (AB + AC) and AC < (AB + BC) :
    print("Z tych odcinków można zbudować trójkąt")
else:
    print("Z tych odcinków nie da się zbudować trójkąta")
print(f'Pole trójkonta wynosi: {round(pole),2} cm2')
