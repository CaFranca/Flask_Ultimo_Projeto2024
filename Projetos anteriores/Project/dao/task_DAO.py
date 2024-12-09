from models import Produto, db

class ProdutoDAO:
    @staticmethod
    def add_produto(codigo, nome, preco, estoque):
        produto = Produto(
            codigo = codigo, 
            nome = nome, 
            preco = preco, 
            estoque = estoque
        )
        db.session.add(produto)
        db.session.commit()
        return produto

    @staticmethod
    def get_produto_por_codigo(codigo):
        produto = Produto.query.get(codigo)
        if not produto:
            return None, "Produto não encontrado"
        
        return produto, None