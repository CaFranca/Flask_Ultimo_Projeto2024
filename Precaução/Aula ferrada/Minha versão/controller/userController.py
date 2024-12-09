from flask import Blueprint, render_template,redirect,url_for, jsonify
from model.user import User
from database import db
from dao import UserDao


userController=Blueprint("user", __name__)

@userController.route("/")
def home():
    return redirect(url_for('user.sla'))

@userController.route("/sla")
def sla():
    return render_template('index.html', mensagem="Abriu", Imagem="Inicio")

@userController.route("/travis")
def travis():
    return render_template('index.html', mensagem="Abriu", Imagem="nada")


@userController.route("/add")
def add():
    retorno = UserDao.add_usuario("Caique", "morra@gmail.com")
    if retorno:
        return "Deu Bom"
    return "Deu merda"

@userController.route("/ver")
def ver():


    return jsonify(LiastaJson)
