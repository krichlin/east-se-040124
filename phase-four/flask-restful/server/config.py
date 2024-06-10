from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import MetaData
from flask_migrate import Migrate

convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'

db = SQLAlchemy(metadata=metadata)

migrate = Migrate(app, db)

db.init_app(app)