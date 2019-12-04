from settings import db


class InfoCodes(object):
    """docstring for InfoCodes"""
    USER_NOT_FOUND = 1
    USERNAME_NOT_FOUND = 2
    EMAIL_NOT_FOUND = 3
    WRONG_PASSWORD = 4
    SUCCESS = 5


class Model:
    """docstring for Model"""

    def __init__(self, session=db.session):
        self.__session = session
    # ------------------------- #
    #       GENERAL METHODS     #
    # ------------------------- #

    def save_changes(self):
        # If there are modifica
        # tions without be added to the tables returns True
        if self.__session.dirty:
            # Update tables
            self.__session.new
        self.__session.commit()

    def undo_changes(self):
        self.__session.rollback()

    def close_session(self):
        self.__session.close()

    # ------------------------- #
    #       USER METHODS        #
    # ------------------------- #

    def create_user(self, username, email, password, name, lastname, phone):
        self.__session.add(User(username=username, email=email,
                                password=password, name=name,
                                lastname=lastname, phone=phone,))

    def read_user(self, username=None, email=None):
        if username:
            response = self.__session.query(User).filter(
                User.username == username).first()
            if response:
                return response
            else:
                return False
        elif email:
            response = self.__session.query(User).filter(
                User.email == email).first()
            if response:
                return response
            else:
                return False
        return False

    def read_users(self):
        return self.__session.query(User).all()

    def update_user(self, user, username=None, email=None,
                    password=None, name=None, lastname=None, phone=None):
        if not user:
            return False
        if username:
            if self.read_user(username=username):
                return False
            if email:
                if self.read_user(email=email):
                    return False
            user.email = email
            user.username = username
        if password:
            user.password = password
        if name:
            user.name = name
        if lastname:
            user.lastname = lastname
        if phone:
            user.phone = phone

        return user

    def delete_user(self, user):
        self.__session.delete(user)

    def verify_user(self, token, password):
        user = self.session.query(User).filter(
            (User.username == token) | (User.email == token)).first()
        if not user:
            return InfoCodes.USER_NOT_FOUND
        if not user.password == password:
            return InfoCodes.WRONG_PASSWORD
        else:
            return InfoCodes.SUCCESS


class User(db.Model):
    """docstring for User"""

    __tablename__ = "User"
    username = db.Column(db.String(30), nullable=False, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
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
