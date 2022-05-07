print(f'____'*25,"Zadanie 1")
""" napisz funkcję wykonującą silnię """

def silnia(liczba: int)->int:
    wynik = 1
    for i in range(1, liczba + 1):
        wynik *= i
    return wynik


print(f'{silnia(5) = }')

print(f'____'*25,"funkcja rekurencyjna - zainteresuj się językami funkcyjnymi")

# 0! = 1
# n! = n *(n-1)!

# def silnia_rekurencyjna(n: int) -> int:
#     if n == 0:
#         return 1
#     return n * silnia_rekurencyjna(n-1)
#
# print(f'{silnia_rekurencyjna(5) = }')

print(f'____'*25,"Zadanie 2")

"""liczby fibonnaciego"""
# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2)

# def ciag_f(n: int) ->int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return ciag_f(n - 1) + ciag_f(n-2)
#
# print(f'{ciag_f(9)}')
"""dokończ w domu bo jest źle"""
# def fib(liczba: int) ->int:
#     wynik1 = 0
#     zmi_1 = 1
#     zmi_2 = 0
#     for a in range(1,liczba):
#         zmi_2 = wynik1 + zmi_1
#         wynik1= zmi_2+zmi_1
#         zmi_1 = wynik1
#     return wynik1
# #
# print(f'{fib(9)}')


print(f'____'*25,"Zadanie 3")

"""funkcja spłaszczajaca listę"""



def splaszcz(lista):
    lista_wynikowa=[]
    for a in lista:
        print(a, type(a))
        if isinstance(a, list):
            for x in splaszcz(a):#wykorzystaliśmy tu rekurencję. Funkcja odwołuje sioesama do siebie
                lista_wynikowa.append(x)
        else:
            lista_wynikowa.append(a)
    return lista_wynikowa



print(splaszcz([1,2,[3,[[[[4]],5]]],5]))