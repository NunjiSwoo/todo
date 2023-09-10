from rest_framework import serializers
from todo.models.categoryEntity import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = '__all__'
