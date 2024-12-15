from flask import Blueprint, render_template,request,session,redirect,url_for,flash
from hashlib import sha256
from DAO import AutorDAO, LivroDAO, CategoriaDAO,UsuarioDAO
from model import Usuarios

# Criação de um Blueprint chamado "bp_authors" para gerenciar rotas relacionadas a autores
padraoController = Blueprint("bp_inicio", __name__)


# Rota inicial para renderizar uma página específica para autores
@padraoController.route("/")
def index():
    return redirect(url_for('bp_inicio.login'))

@padraoController.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"] 
        senha = sha256(request.form.get('senha').encode('utf-8')).hexdigest()
        try:
            user = Usuarios.query.filter((Usuarios.email == usuario) | (Usuarios.nome == usuario)).first()
            if user and user.senha == senha:
                session['usuario'] = user.email
                session['nome'] = user.nome
                session['tipo'] = user.tipo 

                flash(f"Bem-vindo, {user.nome}!", "success")
                return redirect(url_for('bp_inicio.index'))  
            else:
                flash("Usuário ou senha inválidos. Tente novamente.", "error")
        except Exception as e:
            flash(f"Ocorreu um erro ao tentar fazer login: {e}", "error")

        livros=LivroDAO.searchBooksCustom()
        categorias=CategoriaDAO.searchCategories()
        autores=AutorDAO.searchAutores()
        usuarios=UsuarioDAO.listar_todos()
        return render_template("home.html", livros=livros, autores=autores, categorias=categorias,usuarios=usuarios)

    return render_template("login.html")

@padraoController.route("/logout")
def logout():
    session.clear()  # Limpa a sessão
    flash("Você saiu da sua conta.", "success")
    return redirect(url_for('bp_inicio.login'))