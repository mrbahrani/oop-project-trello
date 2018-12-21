from table import Table
from user import User
from models import BoardModel
from abstract_class import AbstractItem


class Board(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = BoardModel

    @property
    def tables(self):
        return self._get_elements_list()

    def add_table(self, table: Table):
        return self._add_element(table)

    def remove_table(self, table: Table):
        return self._remove_element(table)

