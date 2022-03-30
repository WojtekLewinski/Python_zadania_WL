"""Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)

Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze
współczynnik BMI, oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI:
wzór, interpretację wyników, proszę znaleźć samodzielnie)."""

wzrost = int(input("Podaj wzrost w cm"))
masa_ciala = float(input("Podaj masę ciała w kg"))
BMI = round((masa_ciala / (wzrost/100)**2),2)
if BMI <16:
    print(f'BMI: {float(BMI)} Wygłodzenie (niedowaga)')
if BMI >= 16 and BMI < 17:
     print(f'BMI: {float(BMI)} Wychudzenie (niedowaga)')
if BMI >= 17 and BMI < 18.5:
    print(f'BMI: {float(BMI)} Niedowaga')
if BMI >= 18.5 and BMI < 25:
     print(f'BMI: {float(BMI)} Pożądana masa ciała (optimum)')
if BMI >= 25 and BMI < 30:
     print(f'BMI: {float(BMI)} Nadwaga (nadwaga)')
if BMI >= 30 and BMI < 35:
     print(f'BMI: {float(BMI)} Otyłość 1 stopnia (otyłość)')
if BMI >= 35 and BMI < 40:
     print(f'BMI: {float(BMI)} Otyłość 2 stopnia  (duża otyłość)')
if BMI >= 40:
     print(f'BMI: {float(BMI)} Otyłość 3 stopnia (chorobliwa otyłość)')


