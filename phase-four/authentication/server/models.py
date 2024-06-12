from config import db, bcrypt
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-created_at', '-updated_at',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    # 2a. create _password_hash column type string

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # 2b. define property to get _password_hash

    # 2c. define property setter to set _password_hash
        # DO NOT want plain text passwords in the database!

    # 2d. create User instances in flask shell

    # 6b. Create an authenticate method that uses bcyrpt to verify the password against the hash in the DB with bcrypt.check_password_hash

    def __repr__(self):
        return f'<User id={self.id} username={self.username} >'

class Project(db.Model, SerializerMixin):
    __tablename__ = 'projects'

    serialize_rules = ('-created_at','-updated_at',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    about = db.Column(db.String)
    phase = db.Column(db.String)
    link = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Project id={self.id} name={self.name} >'