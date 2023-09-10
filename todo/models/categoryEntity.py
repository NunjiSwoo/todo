from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.descricao
