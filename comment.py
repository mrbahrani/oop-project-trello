class Comment:
    def __init__(self):
        self.id = int()
        self.sender = None
        self.text = None

    def get_sender(self):
        return self.sender

    def set_sender(self, user):
        self.sender = user

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.text = new_text

    def get_id(self):
        return self.id

    def set_id(self, new_id:int):
        self.id = new_id

    def match(self, com):
        if self.id == com.get_id():
            return True
        else:
            return False
