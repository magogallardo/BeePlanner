from settings import db


class User(db.Model):
    """docstring for User"""
    user_id = db.Column(db.Integer, nullable=False, primary_key=True)
    last_name = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTim, nullable=False)
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
    schedule = db.relationship('Schedule', backref='activity')
    reminder = db.relationship('Reminder', backref='activity')
    note = db.relationship('Note', backref='activity')


class Grade(db.Model):
    grade_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    consideration = db.Column(db.Float, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'activity.activity_id'), nullable=False)
    listgrade = db.relationship('ListGrade', backref='grade')


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
    listtask = db.relationship('ListTask', backref='task')


class ListTask(db.Model):
    task_id = db.Column(db.Integer, db.ForeignKey(
        'task.task_id'), nullable=False, primary_key=True)
    list_item = db.Column(db.String(20), nullable=False, primary_key=True)
    # TODO: PRIMARY KEY(task_id, list_item)


class ListGrade(db.Model):
    grade_id = db.Column(db.Integer, db.ForeignKey(
        'grade.grade_id'), nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False, primary_key=True)
    grade = db.Column(db.Float, nullable=False, primary_key=True)
    # TODO: PRIMARY KEY(grade_id, name, grade)


class Schedule(db.Model):
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'activity.activity_id'), nullable=False, primary_key=True)
    time_init = db.Column(db.DateTime, nullable=False, primary_key=True)
    time_finish = db.Column(db.DateTime, nullable=False, primary_key=True)
    day = db.Column(db.String(10), nullable=False, primary_key=True)
    # TODO: PRIMARY KEY(activity_day, activity_time)


class Reminder(db.Model):
    reminder_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False,)
    description = db.Column(db.String(25), nullable=False,)
    reminder_date = db.Column(db.DateTime, nullable=False,)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'activity.activity_id'), nullable=False)


class Note(db.Model):
    note_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(30), nullable=False, )
    note_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'activity.activity_id'), nullable=False)
