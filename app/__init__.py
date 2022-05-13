
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import config_options
from flask_migrate import Migrate
from flask_uploads import UploadSet,configure_uploads,IMAGES

# from config import Config


db = SQLAlchemy()

login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

   


   
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

     # setting config
    from .requests import configure_request
    configure_request(app)
  
    return app



