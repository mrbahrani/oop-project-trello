from card import Card
from models import TableModel
from abstract_class import ComposedItem as AbstractItem


class Table(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = TableModel

    @property
    def cards(self):
        sorted_cards = self._elements_list = sorted(self._elements_list, key=lambda elm: getattr(elm, 'order'))
        return sorted_cards

    def add_card(self, query_manager, card: Card, order=None):
        return self.add_element(query_manager, card, order)

    def remove_card(self, query_manager, card: Card):
        return self._remove_element(query_manager, card)

    def move_card(self, query_manager, card: Card, table, order=None):
        self._move_element(query_manager, card, table, order)

    def reorder_cards(self, query_manager, element=None, index=None):
        return self._reorder_elements(query_manager, element, index)

    def copy_card(self, query_manager, element, parent_element, order=None):
        self._copy_element(query_manager, element, parent_element, order)
