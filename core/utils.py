import requests

def get_book_image(isbn):
    """
    Função que busca a capa do livro utilizando a Google Books API.
    Retorna a URL da imagem ou None se não encontrar.
    """
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()
    
    # Verifica se a resposta contém livros e se a chave 'imageLinks' existe
    if 'items' in data:
        try:
            # Tenta acessar a URL da imagem
            image_url = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
            return image_url
        except KeyError:
            # Caso a chave 'imageLinks' não exista, retorna None
            return None
    return None
