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
        'user.user_id'), nullable=False)
    grade = db.relationship('Grade', backref='activity')
    task = db.relationship('Task', backref='activity')


class Grade(db.Model):
    grade_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    consideration = db.Column(db.Float, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'activity.activity_id'), nullable=False)


class Task(db.Model):
    task_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(20), nullable=False,)
    description = db.Column(db.String(30), nullable=False)
    progress = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'activity.activity_id'), nullable=False)
    list_task = db.relationship('ListTask', backref='task')


class ListTask(db.Model):
    task_id = db.Column(db.Integer, db.ForeignKey(
        'task.id_task'), nullable=False)
    list_item = db.Column(db.String(20), nullable=False)
    # PRIMARY KEY(task_id, list_item)
