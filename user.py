class User:
    def __init__(self):
        self.username = str()
        self.email = str()
        self.name = str()
        self.password = str()

    def set_password(self, password):
        self.password = password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.username

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def match_user(self, user):
        return self.username == user.username and \
               self.name == user.name and \
               self.email == self.name



