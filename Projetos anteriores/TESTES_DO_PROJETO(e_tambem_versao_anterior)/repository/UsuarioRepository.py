from flask import redirect, url_for
from DAO import UsuarioDAO
from datetime import datetime

class UsuarioRepository:
    def __init__(self):
        self.usuarioDAO = UsuarioDAO()

    def novoUsuario(self, nome, email, senha, tipo, data_criacao):
        try:
            # Converte a data_criacao para um objeto datetime.date
            
            
            sucesso = self.usuarioDAO.novo_usuario(nome, email, senha, tipo, data_criacao)
            if sucesso:
                return redirect(url_for("bp_usuario.view_usuarios"))
            return "Erro ao criar o usuario..."
        except Exception as e:
            print(f"Erro no processo de criação do usuario: {e}")
            return "Erro interno ao criar o usuario..."
        
    def listarTodosJSON(self):
        try:
            usuarios = self.usuarioDAO.listar_todos()
            return [usuario.JSonificar() for usuario in usuarios]
        except Exception as e:
            print(f"Erro ao listar todos os usuarios: {e}")
            return []

    def buscarUsuarioPorId(self, usuario_id: int):
        try:
            return self.usuarioDAO.buscar_por_id(usuario_id)
        except Exception as e:
            print(f"Erro ao buscar Usuario por ID: {e}")
            return None

    def atualizar_usuario(self,usuario_id: int, nome,email,senha,tipo,data_criacao: str):
        try:
            sucesso = self.usuarioDAO.atualizar_usuario(usuario_id, nome,email,senha,tipo,data_criacao)
            return "Usuario atualizada com sucesso!" if sucesso else "Erro ao atualizar o usuario..."
        except Exception as e:
            print(f"Erro no processo de atualização de usuario: {e}")
            return "Erro interno ao atualizar o usuario..."

    def deletar_usuario(self, usuario_id: int):
        try:
            sucesso = self.usuarioDAO.deletar_usuario(usuario_id)
            return "Usuario excluído com sucesso!" if sucesso else "Erro ao excluir o Usuario..."
        except Exception as e:
            print(f"Erro no processo de exclusão do Usuario: {e}")
            return "Erro interno ao excluir o Usuario..."

    def listarPorUsuarioJSON(self, usuario_id: int):
        try:
            usuarios = self.usuarioDAO.listar_por_usuario(usuario_id)
            return [usuario.JSonificar() for usuario in usuarios]
        except Exception as e:
            print(f"Erro ao listar empréstimos por usuario: {e}")
            return []

    def listarPorLivroJSON(self, livro_id: int):
        try:
            emprestimos = self.usuarioDAO.listar_por_livro(livro_id)
            return [emprestimo.JSonificar() for emprestimo in emprestimos]
        except Exception as e:
            print(f"Erro ao listar empréstimos por livro: {e}")
            return []


    def usuario_existe_por_email(self, email):
        try:
            usuario = self.usuarioDAO.buscar_por_email(email)
            return usuario
        except Exception as e:
            print(f"Erro ao verificar existência do e-mail: {e}")
            return False

    def usuario_existe_por_nome(self, nome):
        try:
            usuario = self.usuarioDAO.buscar_por_nome(nome)
            return usuario
        except Exception as e:
            print(f"Erro ao verificar existência do nome: {e}")
            return False