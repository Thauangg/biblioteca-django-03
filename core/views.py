from rest_framework import generics, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Livro
from .serializers import LivroSerializer
from rest_framework.response import Response
from rest_framework import status

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['titulo', 'autor__nome', 'categoria__nome']
    ordering_fields = ['titulo', 'ano_publicacao']
    search_fields = ['titulo', 'autor__nome', 'categoria__nome']

    def create(self, request, *args, **kwargs):
        print("Dados recebidos:", request.data)  # Imprime os dados recebidos
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Erros de validação:", serializer.errors)  # Imprime os erros de validação
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            print("Erro ao criar livro:", str(e))  # Imprime qualquer exceção que ocorra
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.shortcuts import render

def home(request):
    livros = Livro.objects.all()
    return render(request, 'home.html', {'livros': livros})
