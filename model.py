from flask_sqlalchemy import SQLAlchemy
from settings import app

db = SQLAlchemy(app)


class User(db.Model):
    """docstring for User"""
    user_id = db.Column(db.Integer, nullable=False, primary_key=True)
    last_name = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    # db.relationship must be in the parent table
    activity = db.relationship('Activity', backref='user')


class Activity(db.Model):
    activity_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    is_subject = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.user_id"), nullable=False)
