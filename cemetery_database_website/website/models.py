#Models our data for the database to help filter organize this data
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#Account info
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

#Directory info that will build or gravesite object
class Directory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(25))
    lot = db.Column(db.Integer)
    first_name = db.Column(db.String(20))
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    date_of_birth = db.Column(db.String(15))
    date_of_death = db.Column(db.String(15))
    reserved = db.Column(db.Boolean)
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(50))
    notes = db.Column(db.String(50))
