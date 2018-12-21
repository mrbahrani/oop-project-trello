from table import Table
from models import BoardModel
from abstract_class import AbstractItem


class Board(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = BoardModel

    @property
    def tables(self):
        return self._get_elements_list()

    def add_table(self, query_manager, table: Table, order=None):
        return self._add_element(query_manager, table, order)

    def remove_table(self, query_manager, table: Table):
        return self._remove_element(query_manager, table)

