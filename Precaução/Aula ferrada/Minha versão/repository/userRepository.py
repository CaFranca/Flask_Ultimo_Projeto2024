from dao import UserDao


class UsrRepository:
    def __init__(self):
        self.userDAO= UserDao()

    def buscar_todos_usuarios_json():
        users= UserDao.buscar_todos_usuarios()
        LiastaJson=[]
        
        for user in users:
            LiastaJson.append(user.toJson())
        return LiastaJson
    
    