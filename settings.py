from flask import Flask
<<<<<<< HEAD

global app
app = FLask(__name__)
=======
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

__all__ = ['app', 'login_manager']  # app it will be shared among all files

db_username = 'hbaena'
db_password = 'BeePlanner123|'
db_name = 'Cinema'

app = Flask(__name__)  # This is the flask object that will be executed and it

# MySql connectr
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost/{}'.format(
    db_username, db_password, db_name)

# Necessary to ignore a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret key
app.config['SECRET_KEY'] = ('110c8ae51a4b5af97be6534caef90e4bb9bdcb'
                            '3380af008f90b23a5d1616bf319bc298105da20fe')
db = SQLAlchemy(app)
# Login manager object for autentication
login_manager = LoginManager(app)
>>>>>>> upstream/master
