from flask import Blueprint, render_template, request, redirect, url_for, flash
from repository import AutorRepository
from datetime import datetime

# Cria o blueprint para a rota de autores
authorController = Blueprint('bp_autores', __name__)

# Instancia o repositório de autores
autor_repo = AutorRepository()

# Exibe todos os autores
@authorController.route("/autores", methods=["GET"])
def view_autores():
    try:
        autores_json = autor_repo.searchAutoresJSON()
        return render_template("Autor/autores.html", autores=autores_json)
    except Exception as e:
        flash(f"Erro ao carregar autores: {e}", "error")
        return render_template("Autor/autores.html", autores=[])

# Adiciona um novo autor
@authorController.route("/autores/adicionar", methods=["POST"])
def add_autor():
    try:
        nome = request.form.get("nome")
        data_nascimentoBruta = request.form.get("data_nascimento")
        nacionalidade = request.form.get("nacionalidade")

        if not nome or not data_nascimentoBruta or not nacionalidade:
            flash("Todos os campos são obrigatórios.", "error")
            return redirect(url_for('bp_autores.view_autores'))
        
        data_nascimento = datetime.strptime(data_nascimentoBruta, '%Y-%m-%d').date()
        mensagem = autor_repo.addAutor(nome, data_nascimento, nacionalidade)
        flash(mensagem, "success" if "sucesso" in mensagem.lower() else "error")
        return redirect(url_for('bp_autores.view_autores'))
    except Exception as e:
        flash(f"Erro ao adicionar autor: {e}", "error")
        return redirect(url_for('bp_autores.view_autores'))

# Edita um autor existente
@authorController.route("/autores/editar/<int:id>", methods=["GET", "POST"])
def edit_autor(id):
    try:
        if request.method == "POST":
            nome = request.form.get("nome")
            data_nascimentoBruta = request.form.get("data_nascimento")
            nacionalidade = request.form.get("nacionalidade")

            if not nome or not data_nascimentoBruta or not nacionalidade:
                flash("Todos os campos são obrigatórios.", "error")
                return redirect(url_for('bp_autores.edit_autor', id=id))

            data_nascimento = datetime.strptime(data_nascimentoBruta, '%Y-%m-%d').date()
            mensagem = autor_repo.updateAutor(id, nome, data_nascimento, nacionalidade)
            flash(mensagem, "success" if "sucesso" in mensagem.lower() else "error")
            return redirect(url_for('bp_autores.view_autores'))
        
        autor = autor_repo.getAutorById(id)
        if not autor:
            flash(f"Autor com ID {id} não encontrado.", "error")
            return redirect(url_for('bp_autores.view_autores'))
        
        return render_template("Autor/AutorEdit.html", autor=autor)
    except Exception as e:
        flash(f"Erro ao editar autor: {e}", "error")
        return redirect(url_for('bp_autores.view_autores'))

# Exclui um autor
@authorController.route("/autores/excluir/<int:id>", methods=["POST","GET"])
def delete_autor(id):
    try:
        mensagem = autor_repo.deleteAutor(id)
        flash(mensagem, "success" if "sucesso" in mensagem.lower() else "error")
    except Exception as e:
        flash(f"Erro ao excluir autor: {e}", "error")
    return redirect(url_for('bp_autores.view_autores'))

# Página inicial redireciona para a lista de autores
@authorController.route("/")
def index():
    return redirect(url_for('bp_autores.view_autores'))
