from django.urls import path
from .views import LivroList, LivroDetail  # Importe as views necessárias

urlpatterns = [
    path('livros/', LivroList.as_view(), name='livros-list'),  # URL para listar e criar livros
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),  # URL para obter, atualizar ou deletar um livro específico
]
