from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
# CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = "logins"
login_manager.init_app(app)

from app.model.data_model import User


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


from app.model import data_model
from app import routes
