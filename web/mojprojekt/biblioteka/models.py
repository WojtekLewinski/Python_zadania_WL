from django.db import models


# Create your models here.
class Autor(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)

    def __str__(self):
        return f'({self.id }) {self.imie} {self.nazwisko}'

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=30)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id }) {self.autor} {self.tytul}'