from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '55A2EFCFA2AE126612B7C9CCE12BA'
    '''
    Hosting der Datenbank lieber lokal?
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://k97841_netzwerke:p32M7aAcvep2jeE@mysql2ec5.netcup.net/k97841_netzwerke'

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .api import api

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

    from .swagger import swagger_ui_blueprint, SWAGGER_URL
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    from .models import User, Note

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    login_manager.login_message = "Bitte melden Sie sich an oder registrieren Sie sich, um auf diese Seite zuzugreifen."

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Datenbank erfolgreich erstellt!')
