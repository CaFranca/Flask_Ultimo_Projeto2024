from flask import Blueprint, request, redirect, url_for, render_template, flash
from repository import UsuarioRepository
from hashlib import sha256
from datetime import datetime

usuarioController = Blueprint('bp_usuario', __name__)
usuariosRepository = UsuarioRepository()


@usuarioController.route('/add', methods=['POST','GET'])
def add_usuario():
    referer = request.referrer # Pega de onde a requisição veio. Ela pode ter sido de dois lugares: Painel de Admin e Cadastro. Utilizo essa variável para redirecionar a pessoa para página certa caso algum erro ocorra. 
    if request.method == "POST":
        try:
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = sha256(request.form.get('senha').encode('utf-8')).hexdigest()
            tipo = request.form.get('tipo')
            
            if referer and "users/add" in referer: #Verifica se a pessoa está vindo do cadastro comum. Caso sim, o tipo do usuário deve ser comum.
                tipo = "Comum"
                
            data_criacao = datetime.now().replace(second=0, microsecond=0)
            if not all([nome, email, tipo, senha, data_criacao]):
                flash("Todos os campos são obrigatórios.", "error")
                return redirect(url_for('bp_usuario.add_usuario'))
            
            # Verifica se o e-mail ou nome já existem usando o repositório
            if usuariosRepository.usuario_existe_por_email(email):
                flash("E-mail já está em uso. Por favor, use outro.", "error")
                return redirect(url_for('bp_usuario.add_usuario'))

            if usuariosRepository.usuario_existe_por_nome(nome):
                flash("Nome de usuário já está em uso. Por favor, escolha outro.", "error")
                return redirect(url_for('bp_usuario.add_usuario'))

            response = usuariosRepository.novoUsuario(nome, email, senha, tipo, data_criacao)
            if isinstance(response, str):
                flash(response, "error")
            else:
                flash("Usuário criado com sucesso!", "success")
            return redirect(url_for('bp_inicio.index')) #Mudar para separar a home do Admin.
        
        except Exception as e:
            flash(f"Erro ao criar usuário: {e}", "error")
            print((f"Erro ao criar usuário: {e}", "error"))
            return redirect(url_for('bp_inicio.index'))
    
    if referer and "sucess" in referer:
        return redirect(url_for('bp_inicio.index'))
    return render_template("registrar.html")


@usuarioController.route('/', methods=['GET'])
def view_usuarios():
    try:
        # Busca todos os usuários para exibição
        usuarios = usuariosRepository.listarTodosJSON()
        return render_template("Usuario/usuarios.html", usuarios=usuarios)
    except Exception as e:
        flash(f"Erro ao carregar os usuários: {e}", "error")
        return render_template("Usuario/usuarios.html", usuarios=[])


@usuarioController.route('/editar/<int:usuario_id>', methods=['GET', 'POST'])
def edit_usuario(usuario_id):
    try:
        if request.method == 'POST':
            # Atualização de dados do usuário
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = sha256(request.form.get('senha').encode('utf-8')).hexdigest()
            tipo = request.form.get('tipo')
            data_criacao = datetime.now().replace(second=0, microsecond=0)

            if not all([nome, email, senha, tipo, data_criacao]):
                flash("Todos os campos são obrigatórios para atualizar.", "error")
                return redirect(url_for('bp_usuario.edit_usuario', usuario_id=usuario_id))

            response = usuariosRepository.atualizar_usuario(usuario_id, nome, email, senha, tipo, data_criacao)
            if "Erro" in response:
                flash(response, "error")
            else:
                flash("Usuário atualizado com sucesso!", "success")

            return redirect(url_for('bp_usuario.view_usuarios'))

        # Recuperação do usuário para exibição no formulário
        usuario = usuariosRepository.buscarUsuarioPorId(usuario_id)
        if not usuario:
            flash("Usuário não encontrado.", "error")
            return redirect(url_for('bp_usuario.view_usuarios'))

        return render_template("Usuario/UsuarioEdit.html", usuario=usuario)
    except Exception as e:
        flash(f"Erro ao editar usuário: {e}", "error")
        return redirect(url_for('bp_usuario.view_usuarios'))


@usuarioController.route('/excluir/<int:usuario_id>', methods=['POST'])
def delete_usuario(usuario_id):
    try:
        response = usuariosRepository.deletar_usuario(usuario_id)
        if "Erro" in response:
            flash(response, "error")
        else:
            flash("Usuário excluído com sucesso!", "success")

        return redirect(url_for('bp_usuario.view_usuarios'))
    except Exception as e:
        flash(f"Erro ao excluir usuário: {e}", "error")
        return redirect(url_for('bp_usuario.view_usuarios'))
