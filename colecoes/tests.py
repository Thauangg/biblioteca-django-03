from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Colecao

class ColecaoTestCase(TestCase):
    def setUp(self):
        # Criando o usuário e a coleção associada a ele
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")
        self.colecao = Colecao.objects.create(nome="Coleção Teste", colecionador=self.user)

    def test_colecao_creation(self):
        """Testa se a coleção é criada corretamente"""
        self.assertEqual(self.colecao.nome, "Coleção Teste")

    def test_create_colecao_authenticated(self):
        """Testa se um usuário autenticado pode criar uma nova coleção"""
        response = self.client.post('/colecoes/', {'nome': 'Nova Coleção', 'descricao': 'Descrição Teste'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Nova Coleção')

    def test_create_colecao_unauthenticated(self):
        """Testa se um usuário não autenticado não pode criar uma coleção"""
        self.client.logout()
        response = self.client.post('/colecoes/', {'nome': 'Coleção Não Autenticada', 'descricao': 'Descrição Teste'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_colecao_as_owner(self):
        """Testa se o colecionador pode editar sua própria coleção"""
        response = self.client.put(f'/colecoes/{self.colecao.id}/', {'nome': 'Coleção Atualizada'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.colecao.refresh_from_db()
        self.assertEqual(self.colecao.nome, 'Coleção Atualizada')

    def test_update_colecao_as_non_owner(self):
        """Testa se um usuário não colecionador não pode editar a coleção de outro usuário"""
        other_user = User.objects.create_user(username="otheruser", password="password123")
        self.client.login(username="otheruser", password="password123")
        response = self.client.put(f'/colecoes/{self.colecao.id}/', {'nome': 'Tentativa de Alteração'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_colecao_as_owner(self):
        """Testa se o colecionador pode excluir sua própria coleção"""
        response = self.client.delete(f'/colecoes/{self.colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_colecao_as_non_owner(self):
        """Testa se um usuário não colecionador não pode excluir a coleção de outro usuário"""
        other_user = User.objects.create_user(username="otheruser", password="password123")
        self.client.login(username="otheruser", password="password123")
        response = self.client.delete(f'/colecoes/{self.colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_colecao(self):
        """Testa se qualquer usuário pode visualizar a coleção"""
        response = self.client.get(f'/colecoes/{self.colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Coleção Teste')

    def test_list_colecoes(self):
        """Testa se qualquer usuário pode listar as coleções"""
        response = self.client.get('/colecoes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
