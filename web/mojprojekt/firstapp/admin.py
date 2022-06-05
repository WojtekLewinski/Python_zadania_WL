from django.contrib import admin

from firstapp.models import Osoba
from firstapp.models import Produkt

# Register your models here.
admin.site.register(Osoba)
admin.site.register(Produkt)