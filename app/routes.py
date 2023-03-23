#Eigenentwicklung
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, BooksForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Books
from werkzeug.urls import url_parse

# Eigenentwicklung in Anlehnung an Beautiful Interactive Tables for your Flask Templates von Miguel Grinberg. Quelle: https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    books = Books.query.all()
    return render_template('index.html', books=books)

#Eigenentwicklung
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Falscher Benutzername oder falsches Passwort!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Anmeldung', form=form)


#Übernommen
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#Eigenentwicklung
@app.route('/registrierung', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Herzlich willkommen, dein Konto wurde erstellt!')
        return redirect(url_for('login'))
    return render_template('registrierung.html', title='Neues Konto erstellen', form=form)


#Eigenentwicklung
@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = BooksForm()
    if form.validate_on_submit():
        books = Books(title=form.title.data, author=form.author.data, isbn=form.isbn.data, thema=form.thema.data)
        db.session.add(books)
        db.session.commit()
        flash('Das neue Buch wurde erfasst.')
        return redirect(url_for('index'))
    return render_template('new.html', title='Neues Buch erfassen', form=form)


#Eigenentwicklung
@app.route('/edit/<id>', methods=['GET','POST'])
@login_required
def edit(id):
    books = Books.query.get(id)
    form = BooksForm()
    if books:
        if form.validate_on_submit():
            books.title = form.title.data
            books.author = form.author.data
            books.isbn = form.isbn.data
            books.thema = form.thema.data
            db.session.commit()
            flash('Die Änderungen wurden gespeichert.')
            return redirect(url_for('index'))
        return render_template('edit.html', title='Buch anpassen', form=form, id=id)
    else:
        flash('Buch nicht gefunden.')
    return redirect(url_for('index'))


#Eigenentwicklung
@app.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    books = Books.query.get(id)
    form = BooksForm()
    if books:
        db.session.delete(books)
        db.session.commit()
        flash('Das Buch wurde gelöscht.')
        return redirect(url_for('index'))
    else:
        flash('Buch nicht gefunden.')
    return redirect(url_for('index'))

#Eigenentwicklung
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='About bookshelf')
