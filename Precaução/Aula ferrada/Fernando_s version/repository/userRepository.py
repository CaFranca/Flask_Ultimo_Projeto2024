from dao import UserDao


class UserRepository:
    def __init__(self):
        self.userDao = UserDao()

    def buscar_todos_usuarios(self):
        users = self.userDao.Buscar_todos_usuarios()
        listajson = []

        for user in users:
            listajson.append(user.toJson())

        return listajson