from flask import Flask
from database import poggers, init_database
from controller import userController

app = Flask(__name__)
init_database(app)
app.register_blueprint(userController)

if __name__ == "__main__":
    app.run(debug=True)