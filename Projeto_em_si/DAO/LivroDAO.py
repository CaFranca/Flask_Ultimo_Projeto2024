from database import database
from model import Livros



class LivroDAO:
    @staticmethod
    def searchBooks():
        # Retorna todos os livros do banco de dados
        return Livros.query.all()

    @staticmethod
    def addBook(titulo, autor_id, editora, ano_publicacao, genero, isbn, quantidade_total, quantidade_disponivel):
        try:
            # Cria um novo objeto Livro
            novo_livro = Livros(
                titulo=titulo,
                autor_id=autor_id,
                editora=editora,
                ano_publicacao=ano_publicacao,
                genero=genero,
                isbn=isbn,
                quantidade_total=quantidade_total,
                quantidade_disponivel=quantidade_disponivel,
            )
            # Adiciona o livro ao banco de dados
            database.session.add(novo_livro)
            # Confirma a transação
            database.session.commit()
            return True
        except Exception as e:
            # Em caso de erro, desfaz a transação
            database.session.rollback()
            print(f"Erro ao adicionar livro: {e}")
            return False

    @staticmethod
    def updateBook(id, titulo, autor_id, editora, ano_publicacao, genero, isbn, quantidade_total, quantidade_disponivel):
        try:
            # Busca o livro pelo ID
            livro = Livros.query.get(id)
            if livro:
                # Atualiza os campos do livro
                livro.titulo = titulo
                livro.autor_id = autor_id
                livro.editora = editora
                livro.ano_publicacao = ano_publicacao
                livro.genero = genero
                livro.isbn = isbn
                livro.quantidade_total = quantidade_total
                livro.quantidade_disponivel = quantidade_disponivel
                # Confirma a transação
                database.session.commit()
                return True
            return False
        except Exception as e:
            # Em caso de erro, desfaz a transação
            database.session.rollback()
            print(f"Erro ao atualizar livro: {e}")
            return False

    @staticmethod
    def getBookById(id):
        # Retorna o livro pelo ID
        return Livros.query.get(id)
    
    @staticmethod
    def getAutores():
        try:
            autores = database.session.query(Livros.autor).distinct().all()
            return [autor[0] for autor in autores]  # Extraindo apenas os nomes
        except Exception as e:
            print(f"Erro ao buscar autores: {e}")
            return []

    @staticmethod
    def getCategoria():
        try:
            generos = database.session.query(Livros.genero).distinct().all()
            return [genero[0] for genero in generos]  # Extraindo apenas os nomes
        except Exception as e:
            print(f"Erro ao buscar gêneros: {e}")
            return []

    @staticmethod
    def deleteBook(id):
        try:
            # Busca o livro pelo ID
            livro = Livros.query.get(id)
            if livro:
                # Exclui o livro
                database.session.delete(livro)
                # Confirma a transação
                database.session.commit()
                return True
            return False
        except Exception as e:
            # Em caso de erro, desfaz a transação
            database.session.rollback()
            print(f"Erro ao excluir livro: {e}")
            return False

    @staticmethod
    def searchBooksCustom(titulo=None, autor_id=None, editora=None, genero=None, ano_inicio=None, isbn=None):
        # Cria a consulta básica para livros
        query = Livros.query

        # Filtro por título, se fornecido
        if titulo:
            query = query.filter(Livros.titulo.like(f"%{titulo}%"))

        # Filtro por autor, se fornecido
        if autor_id:
            query = query.filter(Livros.autor.like(f"%{autor_id}%"))

        # Filtro por editora, se fornecido
        if editora:
            query = query.filter(Livros.editora.like(f"%{editora}%"))

        # Filtro por gênero, se fornecido
        if genero:
            query = query.filter(Livros.genero.like(f"%{genero}%"))

        # Filtro por ano de publicação, se fornecido
        if ano_inicio:
            query = query.filter(Livros.ano_publicacao >= ano_inicio)

        # Filtro por ISBN, se fornecido
        if isbn:
            query = query.filter(Livros.isbn.like(f"%{isbn}%"))

        # Retorna a lista de livros conforme os filtros
        return query.all()
