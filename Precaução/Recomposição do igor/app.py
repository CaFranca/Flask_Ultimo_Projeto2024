from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Lista de produtos (dado simulado, sem usar banco de dados)
produtos = [
    {"id": 1, "nome": "Produto 1", "descricao": "Descrição do Produto 1", "preco": 934.1},
    {"id": 2, "nome": "Produto 2", "descricao": "Descrição do Produto 2", "preco": 456.48},
    {"id": 3, "nome": "Produto 3", "descricao": "Descrição do Produto 3", "preco": 440.94},
    {"id": 4, "nome": "Produto 4", "descricao": "Descrição do Produto 4", "preco": 399.24},
    {"id": 5, "nome": "Produto 5", "descricao": "Descrição do Produto 5", "preco": 300.87},
    {"id": 6, "nome": "Produto 6", "descricao": "Descrição do Produto 6", "preco": 692.51},
    {"id": 7, "nome": "Produto 7", "descricao": "Descrição do Produto 7", "preco": 765.18},
    {"id": 8, "nome": "Produto 8", "descricao": "Descrição do Produto 8", "preco": 99.61},
    {"id": 9, "nome": "Produto 9", "descricao": "Descrição do Produto 9", "preco": 230.29},
    {"id": 10, "nome": "Produto 10", "descricao": "Descrição do Produto 10", "preco": 512.51}
]


# Rota principal: redireciona para a página de produtos
@app.route('/')
def index():
    return redirect(url_for('produtos_list'))

# Rota para listar os produtos com paginação
@app.route('/produtos')
def produtos_list():
    # Obtém o número da página atual (por padrão é 1)
    page = request.args.get('page', 1, type=int)
    per_page = 3  # Definindo quantos produtos exibir por página
    
    # Calculando o intervalo de produtos para exibir
    start = (page - 1) * per_page
    end = start + per_page
    produtos_paginados = produtos[start:end]
    
    # Calculando o total de páginas para navegação
    total_pages = (len(produtos) + per_page - 1) // per_page
    
    # Renderiza o template e passa os dados de produtos, página atual e total de páginas
    return render_template('produtos.html', produtos=produtos_paginados, page=page, total_pages=total_pages)

# Rota para obter os detalhes de um produto em formato JSON
@app.route('/produto/<int:id>', methods=['GET'])
def produto_detalhes(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        return jsonify(produto)
    return jsonify({"error": "Produto não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
