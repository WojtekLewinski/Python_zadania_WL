# Zadanie 1

# cena_za_kg = float(input("Ile kosztuje kilogram ziemniaków?"))
# print(f'Cena za pięć kilogramów ziemniaków to: {cena_za_kg*5} PLN')

print("_" * 68)

"""wersja_2"""

# cena_kg = float(input("Ile kosztuje kilogram ziemniaków?"))
# ile_kupic = float(input("Ile kilogramów chcesz kupić?"))
# print(f'Kwota do zapłacenia to: {cena_kg * ile_kupic} PLN!')

print("_" * 68)

"""wersja_3"""

cena_kg_ziemniakow = float(input("Ile kosztuje kilogram ziemniaków?"))
ile_kupic_ziemniakow = float(input("Ile kilogramów ziemniaków chcesz kupić?"))
cena_kg_bananow = float(input("Ile kosztuje kilogram bananów?"))
ile_kupic_bananow = float(input("Ile kilogramów bananów chcesz kupić?"))
Kwota_do_zapłaty = (cena_kg_ziemniakow * ile_kupic_ziemniakow) + (cena_kg_bananow * ile_kupic_bananow)
if cena_kg_ziemniakow * ile_kupic_ziemniakow > cena_kg_bananow * ile_kupic_bananow:
    print("Za ziemniaki zapłaciłeś wiecej niż za banany:")
elif cena_kg_bananow * ile_kupic_bananow > cena_kg_ziemniakow * ile_kupic_ziemniakow:
    print("Za banany zapłaciłeś więcej niż za ziemniaki")
else:print("Banany i ziemniaki kosztowały tyle samo")
print(f'Kwota do zapłacenia za ziemniaki i banany to: {Kwota_do_zapłaty} PLN!')