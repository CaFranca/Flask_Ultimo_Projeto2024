from flask import Blueprint, jsonify, render_template, redirect, url_for
from DAO import UserDAO
from repository import UserRepository
from model import Posts

userController = Blueprint("bp_user", __name__)
userRepository = UserRepository()

@userController.route("/add")
def add():   
    return userRepository.addUsers("Bruno Melhor do Brasil", "Bruno.mtopog@example.com")

@userController.route("/ver")
def ver():
    return jsonify(userRepository.searchUsersJSON())

@userController.route("/")
def hello():
    return render_template("home.html")