from card import Card
from models import TableModel
from abstract_class import AbstractItem


class Table(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = TableModel

    @property
    def cards(self):
        return self._get_elements_list()

    def add_card(self, query_manager, card: Card, order=None):
        return self._add_element(query_manager, card, order)

    def remove_card(self, query_manager, card: Card):
        return self._remove_element(query_manager, card)

    def move_card(self, query_manager, card: Card, table, order=None):
        self._move_element(query_manager, card, table, order)
