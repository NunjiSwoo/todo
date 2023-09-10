from rest_framework import generics
from rest_framework.response import Response

from todo.models import Categoria
from todo.serializers import CategoriaSerializer  # Você precisa criar este serializer!

class CategoriaListView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get(self, request, *args, **kwargs):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
