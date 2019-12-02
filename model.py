from settings import db


class User(db.Model):
    """docstring for User"""

    __tablename__ = "User"
    user_id = db.Column(db.Integer, nullable=False, primary_key=True)
    last_name = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    # db.relationship must      be in the parent table
    activity = db.relationship('Activity', backref='User')


class Activity(db.Model):
    """docstring for Activity"""

    __tablename__ = "Activity"
    activity_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    is_subject = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'User.user_id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    finish_time = db.Column(db.DateTime, nullable=False)
    monday = db.Column(db.Boolean, nullable=False)
    tuesday = db.Column(db.Boolean, nullable=False)
    wednesday = db.Column(db.Boolean, nullable=False)
    thursday = db.Column(db.Boolean, nullable=False)
    friday = db.Column(db.Boolean, nullable=False)
    saturday = db.Column(db.Boolean, nullable=False)
    sunday = db.Column(db.Boolean, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    # db.relationship must be in the parent table
    task = db.relationship('Task', backref='Activity')


class Task(db.Model):
    """docstring for Task"""

    __tablename__ = "Task"
    task_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(20), nullable=False,)
    description = db.Column(db.String(30), nullable=False)
    progress = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'Activity.activity_id'), nullable=False)


class ListTask(db.Model):
    """docstring for ListTask"""

    __tablename__ = "ListTask"
    task_id = db.Column(db.Integer, db.ForeignKey(
        'task.task_id'), nullable=False, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'task.activity_id'), nullable=False, primary_key=True)
    list_item = db.Column(db.String(20), nullable=False)
    # TODO: PRIMARY KEY(task_id, list_item)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)


class Reminder(db.Model):
    """docstring for Reminder"""

    __tablename__ = "Reminder"
    reminder_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False,)
    description = db.Column(db.String(25), nullable=False,)
    reminder_date = db.Column(db.DateTime, nullable=False,)
    is_all_day = db.Column(db.Boolean, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'Activity.activity_id'), nullable=False)


class Note(db.Model):
    """docstring for Note"""

    __tablename__ = "Note"
    note_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(30), nullable=False, )
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    activity_id = db.Column(db.Integer, db.sForeignKey(
        'Activity.activity_id'), nullable=False)
