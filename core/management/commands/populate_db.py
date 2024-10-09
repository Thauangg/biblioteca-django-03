from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro
from django.utils import timezone

class Command(BaseCommand):
    help = "Popula o banco de dados com dados de exemplo para livros, autores e categorias."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando população do banco de dados...'))

        # Criar Categorias
        self.stdout.write('Criando categorias...')
        categoria_misterio = Categoria.objects.create(nome="Mistério")
        categoria_ficcao = Categoria.objects.create(nome="Ficção")
        categoria_fantasia = Categoria.objects.create(nome="Fantasia")
        categoria_romance = Categoria.objects.create(nome="Romance")
        self.stdout.write(self.style.SUCCESS('Categorias criadas com sucesso!'))

        # Criar Autores
        self.stdout.write('Criando autores...')
        autor_agatha_christie = Autor.objects.create(nome="Agatha Christie")
        autor_arthur_clarke = Autor.objects.create(nome="Arthur C. Clarke")
        autor_conan_doyle = Autor.objects.create(nome="Arthur Conan Doyle")
        autor_cs_lewis = Autor.objects.create(nome="C.S. Lewis")
        autor_emily_bronte = Autor.objects.create(nome="Emily Brontë")
        autor_george_martin = Autor.objects.create(nome="George R.R. Martin")
        autor_isaac_asimov = Autor.objects.create(nome="Isaac Asimov")
        autor_tolkien = Autor.objects.create(nome="J.R.R. Tolkien")
        self.stdout.write(self.style.SUCCESS('Autores criados com sucesso!'))

        # Criar Livros
        self.stdout.write('Criando livros...')
        Livro.objects.create(
            titulo="Assassinato no Expresso do Oriente",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            ano_publicacao=1934,
            publicado_em=timezone.datetime(1934, 1, 1).date(),
        )
        Livro.objects.create(
            titulo="Morte no Nilo",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            ano_publicacao=1937,
            publicado_em=timezone.datetime(1937, 11, 1).date(),
        )
        Livro.objects.create(
            titulo="2001: Uma Odisseia no Espaço",
            autor=autor_arthur_clarke,
            categoria=categoria_ficcao,
            ano_publicacao=1968,
            publicado_em=timezone.datetime(1968, 6, 16).date(),
        )
        Livro.objects.create(
            titulo="Encontro com Rama",
            autor=autor_arthur_clarke,
            categoria=categoria_ficcao,
            ano_publicacao=1973,
            publicado_em=timezone.datetime(1973, 6, 1).date(),
        )
        Livro.objects.create(
            titulo="O Cão dos Baskervilles",
            autor=autor_conan_doyle,
            categoria=categoria_misterio,
            ano_publicacao=1902,
            publicado_em=timezone.datetime(1902, 4, 1).date(),
        )
        Livro.objects.create(
            titulo="As Crônicas de Nárnia",
            autor=autor_cs_lewis,
            categoria=categoria_fantasia,
            ano_publicacao=1950,
            publicado_em=timezone.datetime(1950, 10, 16).date(),
        )
        Livro.objects.create(
            titulo="O Morro dos Ventos Uivantes",
            autor=autor_emily_bronte,
            categoria=categoria_romance,
            ano_publicacao=1847,
            publicado_em=timezone.datetime(1847, 12, 1).date(),
        )
        Livro.objects.create(
            titulo="A Guerra dos Tronos",
            autor=autor_george_martin,
            categoria=categoria_fantasia,
            ano_publicacao=1996,
            publicado_em=timezone.datetime(1996, 8, 6).date(),
        )
        Livro.objects.create(
            titulo="Fundação",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            ano_publicacao=1951,
            publicado_em=timezone.datetime(1951, 6, 1).date(),
        )
        Livro.objects.create(
            titulo="O Senhor dos Anéis",
            autor=autor_tolkien,
            categoria=categoria_fantasia,
            ano_publicacao=1954,
            publicado_em=timezone.datetime(1954, 7, 29).date(),
        )
        self.stdout.write(self.style.SUCCESS('Livros criados com sucesso!'))

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))