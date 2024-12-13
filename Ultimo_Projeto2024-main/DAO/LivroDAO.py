from model import Livros, Autores, Categorias
from database import database


class LivroDAO:
    @staticmethod
    def searchBooks():
        try:
            return Livros.query.all()
        except Exception as e:
            print(f"Erro ao buscar livros: {e}")
            return []

    @staticmethod
    def addBook(titulo, isbn, data_publicacao,  autor_id, categoria_id, quantidade_total):
        try:
            novo_livro = Livros(
                titulo=titulo,
                isbn=isbn,
                data_publicacao=data_publicacao,
                quantidade_total = quantidade_total,
                autor_id=autor_id,
                categoria_id=categoria_id,
            )
            database.session.add(novo_livro)
            print("Livro adicionado!")
            database.session.commit()
            print("Livro commitado!")
            return True
        except Exception as e:
            database.session.rollback()
            print(f"Erro ao adicionar livro: {e}")
            return False

    @staticmethod
    def updateBook(id, titulo, isbn, data_publicacao,  autor_id, categoria_id, quantidade_total):
        try:
            livro = Livros.query.get(id)
            if not livro:
                print(f"Livro com ID {id} não encontrado.")
                return False

            livro.titulo = titulo
            livro.isbn = isbn
            livro.data_publicacao = data_publicacao
            livro.autor_id = autor_id
            livro.categoria_id = categoria_id
            livro.quantidade_total = quantidade_total

            database.session.commit()
            return True
        except Exception as e:
            database.session.rollback()
            print(f"Erro ao atualizar livro: {e}")
            return False

    @staticmethod
    def getBookById(id):
        try:
            return Livros.query.get(id)
        except Exception as e:
            print(f"Erro ao buscar livro por ID: {e}")
            return None

    @staticmethod
    def getAutores():
        try:
            return Autores.query.all()
        except Exception as e:
            print(f"Erro ao buscar autores: {e}")
            return []

    @staticmethod
    def getCategorias():
        try:
            return Categorias.query.all()
        except Exception as e:
            print(f"Erro ao buscar categorias: {e}")
            return []

    @staticmethod
    def deleteBook(id):
        try:
            livro = Livros.query.get(id)
            if not livro:
                print(f"Livro com ID {id} não encontrado.")
                return False

            database.session.delete(livro)
            database.session.commit()
            return True
        except Exception as e:
            database.session.rollback()
            print(f"Erro ao excluir livro: {e}")
            return False

    @staticmethod
    def searchBooksCustom(titulo=None, autor_id=None, categoria_id=None, data_inicio=None, isbn=None):
        try:
            query = Livros.query
            if titulo:
                query = query.filter(Livros.titulo.like(f"%{titulo}%"))
            if autor_id:
                query = query.filter(Livros.autor_id == autor_id)
            if categoria_id:
                query = query.filter(Livros.categoria_id == categoria_id)
            if data_inicio:
                query = query.filter(Livros.data_publicacao >= data_inicio)
            if isbn:
                query = query.filter(Livros.isbn.like(f"%{isbn}%"))
            return query.all()
        except Exception as e:
            print(f"Erro ao realizar consulta personalizada: {e}")
            return []
