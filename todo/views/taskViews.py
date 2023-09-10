from rest_framework import generics
from rest_framework.response import Response

from todo.models import Tarefa
from todo.serializers import TarefaSerializer

class TarefaListView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def get(self, request, *args, **kwargs):
        tarefas = Tarefa.objects.all()  # Correção aqui
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
