from . import db
from enum import unique

# usermixin is custom class that we can inherit and  give our user object sth specific for flask login 
# and flask login is module that help user in login
# userobject needs to inherit from usermixin which needs to beimporte

from flask_login import UserMixin

from sqlalchemy.sql import func

# define class
# general schema
class Note(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(150))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

# usermixin only for user object
class User(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    notes=db.relationship('Note')

