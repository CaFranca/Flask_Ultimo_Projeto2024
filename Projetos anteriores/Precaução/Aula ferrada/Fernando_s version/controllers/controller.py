from flask import Blueprint, jsonify, render_template,redirect,url_for
from dao import UserDao
from repository import UserRepository

userController = Blueprint("user", __name__)
userrepository = UserRepository()

@userController.route("/add")
def add():
    if UserDao.add_usuario("Fernando", "fernando@fernando.com"):
        return render_template('index.html', mensagem="Adicionado", Imagem="Senhor Cinema")
    else:
        return "<p><b>FUDEU!</b></p>"

@userController.route("/ver")
def ver():
    return jsonify(userrepository.buscar_todos_usuarios())


@userController.route("/")
def home():
    return redirect(url_for('user.sla'))

@userController.route("/sla")
def sla():
    return render_template('index.html', mensagem="Abriu", Imagem="Inicio")

@userController.route("/goku")
def goku():
    return render_template('index.html', mensagem="Goku", Imagem="goku")