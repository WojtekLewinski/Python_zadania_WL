class Postac:
    def __init__(self, imie, zdrowie):
        self.imie = imie
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.atak = 0
        self.ekwipunek = []


    def wypisz(self):
        if self.czy_zyje():
            print(f"{self.imie}, {self.zdrowie}/{self.max_zdrowie} HP")
        else:
            print(f"{self.imie}, nie żyje")

    # zmniejsza zdrowie o dmg; zdrowie nie powinno spaść poniżej 0
    def otrzymaj_obrazenia(self, dmg):
        if dmg < 0:
            self.wylecz(-dmg)
            return
        self.zdrowie -= dmg
        if self.zdrowie < 0:
            self.zdrowie = 0

    # przywraca `hp` utraconych punktów zdrowia;
    # zdrowie nie powinno przekroczyć maksymalnej wartosci
    # leczenie nie działa jesli postac nie zyje
    def wylecz(self, hp):
        if hp < 0:
            self.otrzymaj_obrazenia(-hp)
            return
        if self.czy_zyje():
            self.zdrowie += hp
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie
        else:
            print("Nie można wyleczyć trupa!")

    # zwraca iformację, czy postać żyje
    def czy_zyje(self):
        return self.zdrowie > 0

    def daj_atak(self,pkt_atak):
        if pkt_atak > 0:
            self.atak += pkt_atak
        print(f'{self.imie} zadał {self.atak}')

    def przedmiot(self,bron, pkt_broni):
        self.bron = bron
        self.pkt_broni = pkt_broni
        self.ekwipunek.append(bron)
        print(f'{self.imie} otrzymał {self.bron} z bonusem uderzenia {self.pkt_broni}')

    def daj_przedmiot(self, nowa_bron, pkt_nowej_broni):
        if nowa_bron.capitalize not in self.ekwipunek:
            self.ekwipunek.append(nowa_bron)
            print(f'{self.imie} w ekwipunku posiada: {self.ekwipunek}')
        else:
            print(f'{self.imie} w ekwipunku posiada: {self.ekwipunek}')








rufus = Postac("Rufus", 120)
rufus.wypisz() # Rufus, 120/120 HP
rufus.otrzymaj_obrazenia(15)
rufus.wypisz() # Rufus, 105/120 HP
rufus.wylecz(3)
rufus.wypisz() # Rufus, 108/120 HP
rufus.wylecz(30)
rufus.wypisz() # Rufus, 120/120 HP
rufus.otrzymaj_obrazenia(150)
rufus.wypisz() # Rufus, 0/120 HP / Rufus, nie żyje
rufus.wylecz(30)
rufus.wypisz() # Rufus, 0/120 HP / Rufus, nie żyje
rufus.daj_atak(10)
rufus.daj_atak(10)
rufus.przedmiot("Miotła",3)
rufus.daj_przedmiot("Koza",2)
rufus.daj_przedmiot("Myszka", 9)
rufus.daj_przedmiot("Programista nudysta",10)
rufus.ekwipunek
rufus.wypisz() # Rufus, 0/120 HP / Rufus, nie żyje

p = Postac("Worek treningowy", 100)
while p.czy_zyje():
    p.otrzymaj_obrazenia(7)
    p.wypisz()