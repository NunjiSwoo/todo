from rest_framework import serializers
from todo.models.taskEntity import Tarefa
from todo.models.categoryEntity import Categoria

class TarefaSerializer(serializers.ModelSerializer):
    # Defina um queryset para o SlugRelatedField para recuperar as categorias
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(),  # Substitua 'Categoria' pelo nome correto do seu modelo
        slug_field='descricao',
        many=False,  # Você pode ajustar isso dependendo de como deseja lidar com várias categorias
    )
    
    class Meta:
        model = Tarefa
        fields = ['id', 'nome', 'hora', 'dia', 'status', 'categoria']
