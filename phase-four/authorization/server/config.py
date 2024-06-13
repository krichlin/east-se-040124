from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(metadata=metadata)

Migrate(app, db)

db.init_app(app)

api = Api(app)

CORS(app)

# 1. instantiate Bcrypt for password hashing
bcrypt = Bcrypt(app)

# 3b. Session Set up:
# generate a secrete key `python -c 'import os; print(os.urandom(16))'`
# configure secret key with flask app
app.secret_key = b'y$2\xa7l\x89\xb0\t\x87\xb5\x1abf\xff\xeb\xd5'