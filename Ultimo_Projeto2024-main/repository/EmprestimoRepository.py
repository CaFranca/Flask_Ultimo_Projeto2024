from flask import redirect, url_for
from DAO import EmprestimosDAO

class EmprestimosRepository:
    def __init__(self):
        self.emprestimosDAO = EmprestimosDAO()

    def criarEmprestimo(self, usuario_id: int, livro_id: int, data_emprestimo: str, data_devolucao_prevista: str):
        try:
            sucesso = self.emprestimosDAO.criar_emprestimo(usuario_id, livro_id, data_emprestimo, data_devolucao_prevista)
            if sucesso:
                return redirect(url_for("bp_emprestimos.view_emprestimos"))
            return "Erro ao criar o empréstimo..."
        except Exception as e:
            print(f"Erro no processo de criação de empréstimo: {e}")
            return "Erro interno ao criar o empréstimo..."

    def listarTodosJSON(self):
        try:
            emprestimos = self.emprestimosDAO.listar_todos()
            return [emprestimo.JSonificar() for emprestimo in emprestimos]
        except Exception as e:
            print(f"Erro ao listar todos os empréstimos: {e}")
            return []

    def buscarEmprestimoPorId(self, emprestimo_id: int):
        try:
            return self.emprestimosDAO.buscar_por_id(emprestimo_id)
        except Exception as e:
            print(f"Erro ao buscar empréstimo por ID: {e}")
            return None

    def atualizarDevolucao(self, emprestimo_id: int, data_devolucao_real: str):
        try:
            sucesso = self.emprestimosDAO.atualizar_devolucao(emprestimo_id, data_devolucao_real)
            return "Devolução atualizada com sucesso!" if sucesso else "Erro ao atualizar a devolução..."
        except Exception as e:
            print(f"Erro no processo de atualização de devolução: {e}")
            return "Erro interno ao atualizar a devolução..."

    def deletarEmprestimo(self, emprestimo_id: int):
        try:
            sucesso = self.emprestimosDAO.deletar_emprestimo(emprestimo_id)
            return "Empréstimo excluído com sucesso!" if sucesso else "Erro ao excluir o empréstimo..."
        except Exception as e:
            print(f"Erro no processo de exclusão do empréstimo: {e}")
            return "Erro interno ao excluir o empréstimo..."

    def listarPorUsuarioJSON(self, usuario_id: int):
        try:
            emprestimos = self.emprestimosDAO.listar_por_usuario(usuario_id)
            return [emprestimo.JSonificar() for emprestimo in emprestimos]
        except Exception as e:
            print(f"Erro ao listar empréstimos por usuário: {e}")
            return []

    def listarPorLivroJSON(self, livro_id: int):
        try:
            emprestimos = self.emprestimosDAO.listar_por_livro(livro_id)
            return [emprestimo.JSonificar() for emprestimo in emprestimos]
        except Exception as e:
            print(f"Erro ao listar empréstimos por livro: {e}")
            return []
