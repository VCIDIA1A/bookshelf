#Übernommen
from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from flask import url_for

#Übernommen
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self, include_email=False):
        data = {
                'id': self.id,
                'username': self.username,
                }
        if include_email:
            data['email'] = self.email
        return data

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            '_links': {
                'self': url_for('get_user', id=self.id),
            }
        }
        if include_email:
            data['email'] = self.email
        return data

#Übernommen
    @staticmethod
    def to_collection():
        users = User.query.all()
        data = {'items': [item.to_dict() for item in users]}
        return data

#Eigenentwicklung
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    author = db.Column(db.String(140))
    isbn = db.Column(db.String(17))
    thema = db.Column(db.String(40))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Books {}>'.format(self.body)

#Eigenentwicklung
    def to_dict(self):
        bookdata = {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'thema': self.thema,
            '_links': {
                'self': url_for('get_books', id=self.id),
            }
        }
        return bookdata

    @staticmethod
    def to_collection():
        books = Books.query.all()
        bookdata = {'items': [item.to_dict() for item in books]}
        return(bookdata)
