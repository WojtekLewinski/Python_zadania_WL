"""Zadanie 1.4 | Opłata hotelowa (ok 1,5 godz.)

Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a
program wylicza, ile trzeba zapłacić. Zasady są takie:

nieletni (poniżej 18 roku życia) płacą 100 zł za noc
dorośli (ci, którzy mają przynajmniej 18 lat, ale mniej niż 65 lat) płacą:
200 zł za noc, jeśli nocują jedną noc
180 zł za noc, jeśli nocują przynajmniej dwie, ale mniej niż pięć nocy
150 zł za noc, jeśli nocują pięć lub więcej nocy
emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za
noc z 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł"""

wiek = int(input("Prosze podać swój wiek"))
nocleg = int(input("ile dni spędzisz w Hotelu?"))
if wiek <65:
    if wiek < 18:
        print(f'Opłata wynosi 100 PLN za noc - łącznie: {nocleg *100} PLN')
    elif wiek >= 18 and wiek < 65 and nocleg == 1:
        print(f'Opłata wynosi 200 PLN za noc - łącznie: {nocleg * 200} PLN')
    elif wiek >= 18 and wiek < 65 and nocleg > 1 and nocleg < 5:
        print(f'Opłata wynosi 180 PLN za noc - łącznie: {nocleg * 180} PLN')
    elif wiek >= 18 and wiek < 65 and nocleg < 5:
        print(f'Opłata wynosi 150 PLN za noc - łącznie: {nocleg * 150} PLN')
else:
    if nocleg == 1:
        print(f'Opłata wynosi 200 PLN minus 10% zniżki za noc - łącznie: {nocleg * (200 - (200/10))} PLN')
    elif nocleg > 1 and nocleg < 5:
        print(f'Opłata wynosi 180 PLN minus 10% zniżki  za noc - łącznie: {nocleg * (180 - (180/10))} PLN')
    else:
        print(f'Opłata wynosi 150 PLN minus 10% zniżkiza noc - łącznie: {nocleg * (150-(150/10))} PLN')





