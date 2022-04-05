"""
Program losuje liczbę z zakresu od 0 do 999.
Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana
liczba była za duża, czy za mała. Gdy użytkownik poda właściwą liczbę, program wypisuje
gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa
się bisekcją i pełni w informatyce bardzo ważną rolę. Umiejętnie ją stosując powinno się te
zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).
"""

import random
los = random.randint(1, 999)
print(los)
i = 0
while i == 0:
    i = i + 1
    pierwsza_proba = int(input('Wylosowałem liczbę z zakresu  od 1 do 999! spróbuj zgadnąć jaką? Po błędnej odpowiedzi bedę Ci podpowiadął!'))
    if los == pierwsza_proba:
        print(f'GRATULACJE TRAFIŁEŚ - wylosowana liczba to {los} trafiłeś i to już przy pierwszej próbie!!!')
        break
    elif los > pierwsza_proba:
        print(f'Wybrana przez Ciebie liczba {pierwsza_proba} jest mniejsza od wylosowanej ')
    elif los < pierwsza_proba:
        print(f'Wybrana przez Ciebie liczba {pierwsza_proba} jest większa od wylosowanej ')
while i >= 1:
    kolejne_proby = int(input('Spróbuj ponownie'))
    i += 1
    if los > kolejne_proby:
        print(f'Wybrana przez Ciebie liczba {kolejne_proby} jest mniejsza od wylosowanej ')
    elif los < kolejne_proby:
        print(f'Wybrana przez Ciebie liczba {kolejne_proby} jest większa od wylosowanej ')
    else:
        print(f'GRATULACJE TRAFIŁEŚ - wylosowana liczba to {los}, potrzebowałeś na to {i} prób')
        break








