from abstract_class import ItemComponent
from models import CommentModel


class Comment(ItemComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.id = int()
        self.model_class = CommentModel
        self.user = None
        self.text = None

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.text = new_text
