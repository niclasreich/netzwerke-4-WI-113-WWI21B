from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):  # DB Schema, Note Model
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    data = db.Column(db.String(10000))  # Note element data, max 10000 chars
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # DateTime
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign Key, User ID; stores note element to an owner (user)

class User(db.Model, UserMixin):  # DB Schema, User Model, inherit from UserMixin
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    email = db.Column(db.String(150), unique=True)  # Unique email, max 150 chars, unique
    password = db.Column(db.String(150))  # Password, max 150 chars
    first_name = db.Column(db.String(150))  # First Name, max 150 chars
    notes = db.relationship('Note')  # Relationship, Note Model; stores notes to an owner (user) in a (kind of) list