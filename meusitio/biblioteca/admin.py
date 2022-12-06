from django.contrib import admin
from .models import Biblioteca, Livro

# Register your models here.

admin.site.register(Livro)
admin.site.register(Biblioteca)

