from settings import db


class User(db.Model):
    """docstring for User"""

    __tablename__ = "User"
    username = db.Column(db.String(30), nullable=False, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    # db.relationship must      be in the parent table
    activity = db.relationship('Activity', backref='User')


class Activity(db.Model):
    """docstring for Activity"""

    __tablename__ = "Activity"
    activity_id = db.Column(db.Integer, nullable=True, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    username = db.Column(db.Integer, db.ForeignKey(
        'User.username'), nullable=False)
    # db.relationship must      be in the parent table
    note = db.relationship('Note', backref='Activity')


class Note(db.Model):
    """docstring for Note"""

    __tablename__ = "Note"
    note_id = db.Column(db.Integer, nullable=False, primary_key=True)
    content = db.Column(db.String(25), nullable=False)
    priority = db.Column(db.String(30), nullable=False, )
    due_date = db.Column(db.DateTime, nullable=False)
    creationt_date = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.Integer, db.ForeignKey(
        'User.username'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'Activity.activity_id'), nullable=False)


class Schedule(db.Model):
    """docstring for Schedule"""

    __tablename__ = "Schedule"
    monday = db.Column(db.String(25), nullable=False)
    tuesday = db.Column(db.String(25), nullable=False)
    wednesday = db.Column(db.String(25), nullable=False)
    thursday = db.Column(db.String(25), nullable=False)
    friday = db.Column(db.String(25), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'Activity.activity_id'), nullable=False)
