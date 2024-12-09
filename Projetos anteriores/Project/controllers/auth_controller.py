from flask import Blueprint, request, jsonify
from repository import ProdutoRepository

produtosController = Blueprint('product', __name__)

produtoRepository = ProdutoRepository()

@produtosController.route('/add', methods=['POST'])
def add_produto_route():
    data = request.json
    codigo = data.get('codigo')
    nome = data.get('nome')
    preco = data.get('preco')
    estoque = data.get('estoque')

    return produtoRepository.add_produto(codigo, nome, preco, estoque)

@produtosController.route('/produto', methods=['GET'])
def get_produto_route():
    codigo = request.args.get('codigo')

    return produtoRepository.get_produto_por_codigo(codigo)
