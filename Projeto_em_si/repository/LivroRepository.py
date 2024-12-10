from flask import redirect, url_for
from DAO import LivroDAO
from datetime import datetime

class LivroRepository:
    def __init__(self):
        # Cria uma instância do DAO para manipulação dos dados de livros
        self.livroDAO = LivroDAO()

    def searchBooksJSON(self):
        #Busca todos os livros e retorna no formato JSON.
        # Obtém todos os livros no banco de dados
        livros = self.livroDAO.searchBooks()
        # Converte os livros para o formato JSON
        livros_json = [livro.JSonificar() for livro in livros]
        return livros_json

    def addBook(self, titulo, autor, editora, ano_publicacao, genero, isbn, quantidade_total, quantidade_disponivel):

    # Adiciona um novo livro no banco de dados.
        # Chama o método DAO para adicionar o livro
        sucesso = self.livroDAO.addBook(
            titulo, autor, editora, ano_publicacao, genero, isbn, quantidade_total, quantidade_disponivel
        )
        # Se o livro for adicionado com sucesso, redireciona
        if sucesso:
            return redirect(url_for("bp_books.view_books"))
        # Caso contrário, retorna um erro
        return "Erro ao adicionar o livro..."

    def updateBook(self, id, titulo, autor, editora, ano_publicacao, genero, isbn, quantidade_total, quantidade_disponivel):

        #Atualiza um livro existente no banco de dados.
        try:
            # Converte a string da data de publicação para datetime
            data_publicacao_convertida = datetime.strptime(ano_publicacao, '%Y-%m-%d').date()
        except ValueError as e:
            return f"Erro: Data de publicação inválida ({e})"

        try:
            # Chama o método DAO para atualizar o livro
            sucesso = self.livroDAO.updateBook(
                id, titulo, autor, editora, data_publicacao_convertida, genero, isbn, quantidade_total, quantidade_disponivel
            )
            if sucesso:
                return "Livro atualizado com sucesso!"
            else:
                return "Erro ao atualizar o livro no banco de dados..."
        except Exception as e:
            return f"Erro ao processar a atualização: {e}"

    def getBookById(self, id):
        #Obtém um livro específico pelo seu ID.
        return self.livroDAO.getBookById(id)

    def deleteBook(self, id):
        #Exclui um livro pelo ID.
        sucesso = self.livroDAO.deleteBook(id)
        if sucesso:
            return "Livro excluído com sucesso!"
        else:
            return "Erro ao excluir o livro..."

    def searchBooksCustom(self, titulo=None, autor=None, editora=None, genero=None, ano_inicio=None, isbn=None):
        #Realiza uma busca personalizada de livros com base nos filtros fornecidos.
        try:
            # Chama o DAO para realizar a busca com os filtros
            livros = self.livroDAO.searchBooksCustom(titulo, autor, editora, genero, ano_inicio, isbn)
            # Converte os livros encontrados para o formato JSON
            livros_json = [livro.JSonificar() for livro in livros]
            return livros_json
        except Exception as e:
            return f"Erro ao realizar a consulta personalizada: {e}"


    def getAutores(self):
        return self.livroDAO.getAutores()

    def getCategoria(self):
        return self.livroDAO.getCategoria()
