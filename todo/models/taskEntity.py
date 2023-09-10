from django.db import models
from todo.models.categoryEntity import Categoria

class Tarefa(models.Model):
    STATUS = (
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
        # Adicione mais estados aqui, se necessário
    )

    nome = models.CharField(max_length=255)
    dia = models.DateField(null=True, blank=True)
    hora = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS, default='pendente')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    