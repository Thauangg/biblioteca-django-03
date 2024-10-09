# Projeto Biblioteca Django

Este projeto foi desenvolvido como parte de um exercício prático para criar um sistema de gerenciamento de biblioteca usando Django.

## Desenvolvedores

- Thauan de Souza Gonçalves
- Joan Pablo de Souza Rodrigues Da Silva

## Descrição do Projeto

O Projeto Biblioteca é um sistema de gerenciamento para bibliotecas, desenvolvido usando o framework Django. Ele permite o cadastro e gerenciamento de livros, autores, e possivelmente outras funcionalidades relacionadas a uma biblioteca.

## Pré-requisitos

- Python (3.8 ou superior)
- pip (gerenciador de pacotes do Python)
- Git

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/Thauangg/biblioteca-django-v2.git
   cd biblioteca
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```
   python manage.py migrate
   ```

5. Crie um superusuário (opcional):
   ```
   python manage.py createsuperuser
   ```

## Executando o projeto

Para iniciar o servidor de desenvolvimento:
python manage.py runserver
Acesse o projeto em `http://localhost:8000`

## Estrutura do Projeto

O projeto inclui os seguintes apps Django:

- `core`: Contém as funcionalidades principais do sistema de biblioteca.



