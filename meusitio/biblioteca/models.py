from django.db import models

# Create your models here.


class Biblioteca(models.Model):
    nome      = models.CharField(max_length=100, verbose_name="nome")
    descricao = models.TextField(max_length=2000, verbose_name="descrição", default="sem descrição")

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo      = models.CharField(max_length=100, verbose_name="título")
    quantidade  = models.IntegerField(verbose_name="quantidade")
    codigo_isbn = models.CharField(max_length=13, unique=True, verbose_name="código ISBN")
    descricao   = models.TextField(max_length=2000, verbose_name="descrição", default="sem descrição")
    biblioteca  = models.ForeignKey(to=Biblioteca, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo