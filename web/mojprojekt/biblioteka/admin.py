from django.contrib import admin

from biblioteka.models import Autor
from biblioteka.models import Ksiazka

# Register your models here.
admin.site.register(Autor)
admin.site.register(Ksiazka)