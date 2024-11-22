from rest_framework import serializers
from .models import Livro, Autor, Categoria
from django.utils import timezone

# Serializador para o modelo Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

# Serializador para o modelo Autor
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']

# Serializador para o modelo Livro
class LivroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()  # Usando o serializador de Autor para retornar mais detalhes
    categoria = CategoriaSerializer()  # Usando o serializador de Categoria
    ano_publicacao = serializers.IntegerField(default=timezone.now().year)  # Valor padrão como o ano atual
    publicado_em = serializers.DateField(default=timezone.now)  # Valor padrão como a data atual

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'categoria', 'ano_publicacao', 'publicado_em', 'isbn']

    def create(self, validated_data):
        # O Django já cuida da conversão correta de campos do tipo DateField, então não há necessidade de verificar manualmente
        return super().create(validated_data)

# Serializador para criar/atualizar livros (usando IDs de autor e categoria)
class LivroCreateUpdateSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())  # Usando o campo de ID
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())  # Usando o campo de ID
    publicado_em = serializers.DateField(default=timezone.now)  # Usando timezone.now diretamente

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'categoria', 'publicado_em']
