from rest_framework import serializers
from .models import Livro, Autor, Categoria
from django.utils import timezone
from datetime import datetime  # Adicionado esta importação

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
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    ano_publicacao = serializers.IntegerField(default=timezone.now().year)
    publicado_em = serializers.DateField(default=timezone.now().date())  # Modificado esta linha

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'categoria', 'ano_publicacao', 'publicado_em', 'isbn']

    def create(self, validated_data):
        if 'publicado_em' in validated_data:
            if isinstance(validated_data['publicado_em'], datetime):
                validated_data['publicado_em'] = validated_data['publicado_em'].date()
        return super().create(validated_data)

# Serializador para criar/atualizar livros (usando IDs de autor e categoria)
class LivroCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'categoria', 'publicado_em']
