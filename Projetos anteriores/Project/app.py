from flask import Flask
from flask_cors import CORS
from database import init_db
from controllers import produtosController

app = Flask(__name__)
cors = CORS(app, resources={r"/produtos/*": {"origins": "*"}})

app.register_blueprint(produtosController, url_prefix='/produtos')

if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)
