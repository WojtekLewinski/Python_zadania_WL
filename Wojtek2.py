"""Zadanie 1.2 | Buty do szewca (ok. 1 godz.)
Napisz taki program:
 użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
(poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci
wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni"""

dzien_oddania = int(input("Podaj numer dnia tygodnia:"))
dni_naprawy = int(input("Ile dni bedzie trwała naprawa:"))
wynik = dzien_oddania + dni_naprawy
if wynik >=1 and wynik <= 7:
    print(f'Dzień odbioru to: {wynik}')
if wynik > 7 and wynik <= 14:
    print(f'Dzień odbioru to: {wynik-7}')
elif wynik > 14 and wynik <=21:
    print(f'Dzień odbioru to: {wynik - 14}')
elif wynik > 21 and wynik <= 28:
    print(f'Dzień odbioru to: {wynik - 21}')
elif wynik > 28 and wynik <=35:
    print(f'Dzień odbioru to: {wynik - 28}')

