from flask_sqlalchemy import SQLAlchemy

poggers = SQLAlchemy()

def init_database(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pogba.db"
    with app.app_context():
        poggers.init_app(app)
        poggers.create_all()