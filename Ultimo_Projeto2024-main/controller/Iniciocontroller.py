from flask import Blueprint, render_template
from DAO import AutorDAO, LivroDAO, CategoriaDAO, EmprestimoDAO,UsuarioDAO

# Criação de um Blueprint chamado "bp_authors" para gerenciar rotas relacionadas a autores
padraoController = Blueprint("bp_inicio", __name__)


# Rota inicial para renderizar uma página específica para autores
@padraoController.route("/")
def index():
    livros=LivroDAO.searchBooksCustom()
    categorias=CategoriaDAO.searchCategories()
    autores=AutorDAO.searchAutores()
    usuarios=UsuarioDAO.listar_todos()
    return render_template("home.html", livros=livros, autores=autores, categorias=categorias,usuarios=usuarios)
