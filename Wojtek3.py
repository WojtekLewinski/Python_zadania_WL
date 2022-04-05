"""Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)

Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze
współczynnik BMI, oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI:
wzór, interpretację wyników, proszę znaleźć samodzielnie)."""

wzrost = int(input("Podaj wzrost w cm"))
masa_ciala = float(input("Podaj masę ciała w kg"))
bmi = round((masa_ciala / (wzrost/100)**2),2)
if bmi <16:
    print(f'BMI: {float(bmi)} Wygłodzenie (niedowaga)')
if bmi >= 16 and bmi < 17:
     print(f'BMI: {float(bmi)} Wychudzenie (niedowaga)')
if bmi >= 17 and bmi < 18.5:
    print(f'BMI: {float(bmi)} Niedowaga')
if bmi >= 18.5 and bmi < 25:
     print(f'BMI: {float(bmi)} Pożądana masa ciała (optimum)')
if bmi >= 25 and bmi < 30:
     print(f'BMI: {float(bmi)} Nadwaga (nadwaga)')
if bmi >= 30 and bmi < 35:
     print(f'BMI: {float(bmi)} Otyłość 1 stopnia (otyłość)')
if bmi >= 35 and bmi < 40:
     print(f'BMI: {float(bmi)} Otyłość 2 stopnia  (duża otyłość)')
if bmi >= 40:
     print(f'BMI: {float(bmi)} Otyłość 3 stopnia (chorobliwa otyłość)')


