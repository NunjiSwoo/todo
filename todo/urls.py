from django.urls import path
from .views import TarefaListView, CategoriaListView

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('tarefas/', TarefaListView.as_view(), name='tarefa-list'),
]
