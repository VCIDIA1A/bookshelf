#Übernommen
from app import app
from app.models import User, Books
from flask import jsonify

#Übernommen
@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    data = User.query.get_or_404(id).to_dict()
    return jsonify(data)
@app.route('/api/users', methods=['GET'])
def get_users():
    data = User.to_collection()
    return jsonify(data)


#Eigenentwicklung
@app.route('/api/books/<id>', methods=['GET'])
def get_books(id):
    data = Books.query.get_or_404(id).to_dict()
    bookdata = Books.to_collection()
    return jsonify(data)
@app.route('/api/books', methods=['GET'])
def get_books2():
    bookdata = Books.to_collection()
    return jsonify(bookdata)
