from settings import db
from model import Model, InfoCodes


class Controller:
    """docstring for Controller"""

    def __init__(self):
        self.model = Model(session=db.session)

    def __del__(self):
        self.model.close_session()

    def undo(self):
        self.model.undo_changes()

    def save(self):
        self.model.save_changes()

    def login(self, token, password):
        return self.model.verify_user(token, password)

    def add_user(self, username, email, password, name, lastname, phone):
        if self.model.read_user(username=username) or \
                self.model.read_user(email=email):
            return InfoCodes.USER_ALREADY_EXIST
        self.model.create_user(username, email, password,
                               name, lastname, phone)
        return InfoCodes.SUCCESS

    def get_username(self, email):
        return self.model.read_user(email=email).username

    def get_all_users(self):
        return self.model.read_users()
