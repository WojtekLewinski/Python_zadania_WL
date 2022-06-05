from django.db import models

# Create your models here.
class Osoba(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)

    def __str__(self):
        return f'({self.id }) {self.imie} {self.nazwisko}'


class Produkt(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField()
    cena = models.IntegerField()
    dostepnosc = models.BooleanField()

    def __str__(self):
        return f'({self.id }) {self.nazwa} '