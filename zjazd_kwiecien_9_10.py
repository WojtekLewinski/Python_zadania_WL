"""
Napisz program wypisujący na konsolę tabliczkę mnożenia
dla liczb od 0 do 10 w postaci tabelki.

       0   1   2   3   4   5   6   7   8   9  10

0      0   0   0   0   0   0   0   0   0   0   0
1      0   1   2   3   4   5   6   7   8   9  10
2      0   2   4   6   8  10  12  14  16  18  20
3      0   3   6   9  12  15  18  21  24  27  30
4      0   4   8  12  16  20  24  28  32  36  40
5      0   5  10  15  20  25  30  35  40  45  50
6      0   6  12  18  24  30  36  42  48  54  60
7      0   7  14  21  28  35  42  49  56  63  70
8      0   8  16  24  32  40  48  56  64  72  80
9      0   9  18  27  36  45  54  63  72  81  90
10     0  10  20  30  40  50  60  70  80  90 100
"""
""" poniżej moja propozycja """
# zmienna_a = 0
# zmienna_b = 0
# while zmienna_a < 10:
#     zmienna_a * zmienna_b
#     zmienna_a =zmienna_a +1
#     print(zmienna_a)


# print(" "*5, end=" ")
# for a in range(0,11):
#     print(f'{a:5}', end=' ')
# print()
# print()
#
# for x in range(0, 11):
#     print(f'{x:<5}',end=" ")
#     for y in range(0,11):
#         print(f'{x * y:5}', end=' ')
#     print()


# print("_"*65, "nowe zadanie")

# """ enumeracja zaczyna od 0 i wyświetla wartość """
# temperatura = [10,15,17,-1,-5,0,2]
# for temperatura in enumerate(temperatura):
#     print(f'index: {temperatura[0]}, wartość: {temperatura[1]}')

"""mozna przypisywać wartości bezpośrednio do tupli lub listy. przykład poniżej.
 Liczba zmiennych i liczba elementów musi być taka sama inaczej dostajemy błąd"""
imie,nazwisko,wiek= ('Wojciech','Lewinski', '45')
print(imie)
print(nazwisko)
print(wiek)
