from database import database
from model import Emprestimos, Usuarios,Livros

class EmprestimosDAO:
    @staticmethod
    def criar_emprestimo(usuario_id, livro_id, data_emprestimo, data_devolucao_prevista):
        emprestimo = Emprestimos(
            usuario_id=usuario_id,
            livro_id=livro_id,
            data_emprestimo=data_emprestimo,
            data_devolucao_prevista=data_devolucao_prevista
        )
        database.session.add(emprestimo)
        database.session.commit()
        return emprestimo

    @staticmethod
    def listar_todos():
        return Emprestimos.query.all()

    @staticmethod
    def buscar_por_id(emprestimo_id):
        return Emprestimos.query.get(emprestimo_id)

    @staticmethod
    def atualizar_devolucao(emprestimo_id, usuario_id, livro_id, data_emprestimo, data_devolucao_prevista):
        emprestimo = Emprestimos.query.get(emprestimo_id)
        if emprestimo:
            emprestimo.usuario_id = usuario_id,
            emprestimo.livro_id = livro_id,
            emprestimo.data_emprestimo = data_emprestimo,
            emprestimo.data_devolucao_prevista = data_devolucao_prevista,
            database.session.commit()
            return emprestimo
        return None

    @staticmethod
    def deletar_emprestimo(emprestimo_id):
        emprestimo = Emprestimos.query.get(emprestimo_id)
        if emprestimo:
            database.session.delete(emprestimo)
            database.session.commit()
            return True
        return False

    @staticmethod
    def listar_por_usuario(usuario_id):
        return Emprestimos.query.filter_by(usuario_id=usuario_id).all()

    @staticmethod
    def listar_por_livro(livro_id):
        return Emprestimos.query.filter_by(livro_id=livro_id).all()
    
    @staticmethod
    def getUsuarios():
        try:
            return Usuarios.query.all()
        except Exception as e:
            print(f"Erro ao buscar autores: {e}")
            return []

    @staticmethod
    def getLivros():
        try:
            return Livros.query.all()
        except Exception as e:
            print(f"Erro ao buscar livros: {e}")
            return []
