from database import database
from model import Autores

class AutorDAO:
    @staticmethod
    def getAllAutores():
        return Autores.query.all()

    @staticmethod
    def addAutor(nome):
        try:
            novo_autor = Autores(nome=nome)
            database.session.add(novo_autor)
            database.session.commit()
            return True
        except Exception as e:
            database.session.rollback()
            print(f"Erro ao adicionar autor: {e}")
            return False

    @staticmethod
    def updateAutor(id, nome):
        try:
            autor = Autores.query.get(id)
            if autor:
                autor.nome = nome
                database.session.commit()
                return True
            return False
        except Exception as e:
            database.session.rollback()
            print(f"Erro ao atualizar autor: {e}")
            return False

    @staticmethod
    def deleteAutor(id):
        try:
            autor = Autores.query.get(id)
            if autor:
                database.session.delete(autor)
                database.session.commit()
                return True
            return False
        except Exception as e:
            database.session.rollback()
            print(f"Erro ao excluir autor: {e}")
            return False

    @staticmethod
    def getAutorById(id):
        return Autores.query.get(id)

    @staticmethod
    def searchAutoresByName(nome):
        return Autores.query.filter(Autores.nome.like(f"%{nome}%")).all()
