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

    def add_card(self, card: Card):
        return self._add_element(card)

    def remove_card(self, card: Card):
        return self._remove_element(card)

    def move_card(self, card: Card, table, order):
        pass
