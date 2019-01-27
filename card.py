# from abstract_class import ComposedItem as AbstractItem
from abstract_class import ComposedItem as AbstractItem
from models import CardModel


class Card(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = CardModel
        # self.comment_list = list()

    @property
    def comments(self):
        return self._get_elements_list()

    def add_comment(self, query_manager, comment, order=None):
        return self.add_element(query_manager, comment, order)

    def remove_comment(self, query_manager, comment):
        self._remove_element(query_manager, comment)
