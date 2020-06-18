from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
import sqlacodegen

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SECRET_KEY'] = '$ecurekey4app'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://capstn:cap@localhost/supermarket"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_BINDS'] = {
    'cpstnpro': "postgresql://capstn:cap@localhost/spmdb"
}

db = SQLAlchemy(app)

# enable CORS
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page
login_manager.login_message_category = "info"  # customize the flash message category


app.config.from_object(__name__)
from app import views
