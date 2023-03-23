#Eigenentwicklung
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Books

#Eigenentwicklung
class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Zugangsdaten merken')
    submit = SubmitField('Anmelden')

#Eigenentwicklung
class RegistrationForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    email = StringField('E-Mail-Adresse', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    password2 = PasswordField(
        'Passwort nochmal eingeben', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Neu Registrieren')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Bitte verwende einen anderen Benutzernamen. Der eingegebene Benutzername existiert bereits.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Bitte verwende eine andere E-Mail-Adresse. Die eingegebene E-Mail-Adresse existiert bereits.')

#Eigenentwicklung
class BooksForm(FlaskForm):
    title = StringField('Buchtitel', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    thema = SelectField('Thema/Genre', choices=[('Krimi'), ('Thriller'), ('Science Fiction'), ('Roman'), ('Sachbuch'), ('Fantasy'), ('Biografie'), ('Kinderbuch')])
    submit = SubmitField('Erfassen')
