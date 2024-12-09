from flask import Flask
from database import init_bd
from controllers import userController


app = Flask(__name__)

init_bd(app)
app.register_blueprint(userController)


if __name__ == "__main__":
    app.run(debug=True)