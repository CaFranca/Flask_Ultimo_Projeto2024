from flask import redirect, url_for
from DAO import LivroDAO
from datetime import datetime

class LivroRepository:
    def __init__(self):
        # Cria uma instância do DAO para manipulação dos dados de livros
        self.livroDAO = LivroDAO()

    def searchBooksJSON(self):
        # Busca todos os livros e retorna no formato JSON.
        livros = self.livroDAO.searchBooks()
        # Converte os livros para o formato JSON
        livros_json = [livro.JSonificar() for livro in livros]
        return livros_json

    def addBook(self, titulo, autor, editora, ano_publicacao, genero, isbn, quantidade_total, quantidade_disponivel):
        # Adiciona um novo livro no banco de dados.
        try:
            # Chama o método DAO para adicionar o livro
            sucesso = self.livroDAO.addBook(
                titulo=titulo,
                autor=autor,
                editora=editora,
                ano_publicacao=ano_publicacao,
                genero=genero,
                isbn=isbn,
                quantidade_total=quantidade_total,
                quantidade_disponivel=quantidade_disponivel
            )
            # Se o livro for adicionado com sucesso, redireciona
            if sucesso:
                return redirect(url_for("bp_books.view_books"))
            return "Erro ao adicionar o livro..."
        except Exception as e:
            return f"Erro ao processar a solicitação de adicionar livro: {e}"

    def updateBook(self, id, titulo, autor, editora, ano_publicacao, genero, isbn, quantidade_total, quantidade_disponivel):
        # Atualiza um livro existente no banco de dados.
        try:
            # Chama o método DAO para atualizar o livro
            sucesso = self.livroDAO.updateBook(
                id=id,
                titulo=titulo,
                autor=autor,
                editora=editora,
                ano_publicacao=ano_publicacao,
                genero=genero,
                isbn=isbn,
                quantidade_total=quantidade_total,
                quantidade_disponivel=quantidade_disponivel
            )
            if sucesso:
                return "Livro atualizado com sucesso!"
            return "Erro ao atualizar o livro no banco de dados..."
        except Exception as e:
            return f"Erro ao processar a atualização: {e}"

    def getBookById(self, id):
        # Obtém um livro específico pelo seu ID.
        return self.livroDAO.getBookById(id)

    def deleteBook(self, id):
        # Exclui um livro pelo ID.
        try:
            sucesso = self.livroDAO.deleteBook(id)
            if sucesso:
                return "Livro excluído com sucesso!"
            return "Erro ao excluir o livro..."
        except Exception as e:
            return f"Erro ao excluir o livro: {e}"

    def searchBooksCustom(self, titulo=None, autor=None, editora=None, genero=None, ano_inicio=None, isbn=None):
        # Realiza uma busca personalizada de livros com base nos filtros fornecidos.
        try:
            livros = self.livroDAO.searchBooksCustom(
                titulo=titulo,
                autor=autor,
                editora=editora,
                genero=genero,
                ano_inicio=ano_inicio,
                isbn=isbn
            )
            livros_json = [livro.JSonificar() for livro in livros]
            return livros_json
        except Exception as e:
            return f"Erro ao realizar a consulta personalizada: {e}"

    def getAutores(self):
        # Obtém a lista de autores disponíveis.
        return self.livroDAO.getAutores()

    def getCategoria(self):
        # Obtém a lista de categorias disponíveis.
        return self.livroDAO.getCategoria()