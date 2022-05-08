# """oerator dostępu"""

# napis= 'Ala ma kota kot ma kompilator'
# print(napis)
# print(napis[0:10])
# print(napis[0:10:2])#co drugi znak od 0 do 10
# print(napis[::-1]) # od tyłu i przydaje siędo sprawdzenia czy zdanei jest palindromem
# print(napis.upper())# wielkie litery
# print(napis.lower())# małe liter
# print(napis.capitalize())# zmienia pierwszą literę na wielką a wszystkie pozostałe na małe.
# # jeżeli w zdaniu jest kropka od nowego zdania nie zmienia na wwielkie
# print(napis.title())# każde słowo z dużej litery
# print(napis.split())# kroi zdanie na sekcje i możemy podać jaki znak będzie separatorem
# print(napis.count('a')) #licza wystąpienia wpisanego znaku
# print(napis.index('a')) # podaje nr indeksu wystąpnienia pierwszej literki a./
# # Python szuka dokładnie takiego znaku jaki wpisaliśmny więc podaj 2 - małe a występuje jako 3

# map - dostaje funkcję i listę i aplikuje tę funkcę do wszystkich elementów listy
# filter - dostaje funkcję i listę aplikuje tę funkcę do każdego elemeentu listy jeżeli funkcje zwróci true
# lambda - funkcja anonimowa - pozwala stworzyć funkcjenie przypisując jej nazwy

napis = "Ala ma kota"
wystapienia = {litera: napis.count(litera) for litera in napis}

# napis = "Ala ma kota"
# wystapienie = {}
# for litera in napis.lower():
#     if litera in wystapienie:
#         wystapienie[litera] += 1
#     else:
#         wystapienie[litera] += 1
#
print(wystapienie)



