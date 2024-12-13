from flask import Blueprint, render_template, redirect, url_for, request, flash
from repository import CategoriaRepository

# Criação de um Blueprint para gerenciar rotas relacionadas a categorias
categoryController = Blueprint("bp_categories", __name__)
# Instancia o repositório de categorias
categoryRepository = CategoriaRepository()

# Rota para adicionar uma nova categoria ao banco de dados
@categoryController.route("/add", methods=['GET', 'POST'])
def add_category():
    if request.method == "POST":
        nome = request.form.get('categoria')
        if not nome:
            flash("O nome da categoria é obrigatório.", "error")
            return redirect(url_for('bp_categories.view_categories'))
        
        mensagem = categoryRepository.addCategory(nome)
        if "sucesso" in mensagem.lower():
            flash(mensagem, "success")
        else:
            flash(mensagem, "error")
        
        return redirect(url_for('bp_categories.view_categories'))
    
    return render_template('Categorias/CategoriaAdd.html')

# Rota para visualizar todas as categorias
@categoryController.route('/categorias', methods=['GET'])
def view_categories():
    nome = request.args.get('nome', '').strip()
    categorias = categoryRepository.searchCategories(nome)
    return render_template('Categorias/categorias.html', categorias=categorias, nome=nome)

# Rota para editar uma categoria existente
@categoryController.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    categoria = categoryRepository.getCategoryById(id)

    if not categoria:
        flash(f"Categoria com ID {id} não encontrada.", "error")
        return redirect(url_for('bp_categories.view_categories'))

    if request.method == 'POST':
        nome = request.form.get('categoria')
        if not nome:
            flash("O nome da categoria é obrigatório.", "error")
            return redirect(url_for('bp_categories.edit_category', id=id))
        
        mensagem = categoryRepository.updateCategory(id, nome)
        if "sucesso" in mensagem.lower():
            flash(mensagem, "success")
        else:
            flash(mensagem, "error")
        
        return redirect(url_for('bp_categories.view_categories'))
    
    return render_template('Categorias/CategoriaEdit.html', categoria=categoria)

# Rota para excluir uma categoria
@categoryController.route('/excluir/<int:id>', methods=['POST'])
def delete_category(id):
    mensagem = categoryRepository.deleteCategory(id)
    if "sucesso" in mensagem.lower():
        flash(mensagem, "success")
    else:
        flash(mensagem, "error")
    return redirect(url_for('bp_categories.view_categories'))
