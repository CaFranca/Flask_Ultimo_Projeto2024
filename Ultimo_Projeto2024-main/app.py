from flask import Flask
# Importa a configuração do banco de dados e as funções para inicialização
from database import init_database
from controller.AutorController import authorController
from controller.LivroController import livroController
from controller.CategoriasController import categoryController
from controller.Iniciocontroller import padraoController
from controller.EmpresimoController import emprestimoController


app = Flask(__name__)
app.secret_key = '4a466f32ff8af1aad05ac24b5eced2531da40d014c105d9f67caf44c73fd73fc'


init_database(app)

app.register_blueprint(emprestimoController, url_prefix="/loan")
app.register_blueprint(authorController, url_prefix="/authors")
app.register_blueprint(livroController, url_prefix="/books")
app.register_blueprint(categoryController, url_prefix="/categories")
app.register_blueprint(padraoController, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
