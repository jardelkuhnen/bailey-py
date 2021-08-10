


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserRepository(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    phone = db.Column(db.String)

    def __init__(self, name):
        self.name = name