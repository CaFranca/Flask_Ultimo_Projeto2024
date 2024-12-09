from flask import Flask, render_template, redirect, url_for, jsonify
from database import init_db
from controller.userController import userController as user

app= Flask(__name__)
app.register_blueprint(user)

init_db(app)
       

if __name__ == '__main__':

    app.run(debug=True)