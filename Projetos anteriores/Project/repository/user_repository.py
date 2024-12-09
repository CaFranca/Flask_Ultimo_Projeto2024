from flask import jsonify
from dao import ProdutoDAO

class ProdutoRepository:
    def __init__(self) -> None:
        self.produtoDao = ProdutoDAO()

    def add_produto(self, codigo, nome, preco, estoque):
        if not all([codigo, nome, preco, estoque]):
            return jsonify({"error": "Faltando informações"}), 400
        
        if len(codigo) != 64:
            return jsonify({"error": "Código inválido"}), 400
        
        produto = self.produtoDao.add_produto(codigo, nome, preco, estoque)
        
        return jsonify({
            "codigo": produto.codigo,
            "nome": produto.nome,
            "preco": produto.preco,
            "estoque": produto.estoque
        }), 201

    def get_produto_por_codigo(self, codigo):
        if not codigo:
            return jsonify({"error": "Faltando código"}), 400
        
        if len(codigo) != 64:
            return jsonify({"error": "Código inválido"}), 400
        
        produto, error = self.produtoDao.get_produto_por_codigo(codigo)
        
        if error:
            return jsonify({"error": error}), 403
        
        return jsonify({
            "codigo": produto.codigo,
            "nome": produto.nome,
            "preco": produto.preco,
            "estoque": produto.estoque
        })
