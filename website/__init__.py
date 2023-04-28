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
    Hosting a Database on a different Server (e.g. MySQL)?
    Replace the sqlite:/// URL with a MySQL URL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://k97841_netzwerke:E5zi8fE08@10.35.46.197:3306/k97841_netzwerke'
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .api import api

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

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