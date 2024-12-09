from flask import redirect, url_for
from DAO import UserDAO

class UserRepository():
    def __init__(self):
        self.userDAO = UserDAO()
    
    def searchUsersJSON(self): #FALTA ARRUMAR O N+1
        users = UserDAO.searchUsers()
        listaJSON = []
        for user in users:
            listaJSON.append(user.JSonificar())
        return listaJSON
    
    def addUsers(self, nome, email):
        retorno = UserDAO.addUsers(nome, email)
        if retorno:
            return redirect(url_for("bp_user.hello"))
        return "Erro ao adicionar..."