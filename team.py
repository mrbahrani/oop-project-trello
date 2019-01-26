from user import User
from board import Board
from abstract_class import ComposedItem as AbstractItem
from models import TeamModel


class Team(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = TeamModel

    @property
    def boards(self):
        return self._get_elements_list()

    def add_board(self, query_manager, board: Board, order=None):
        return self._add_element(query_manager, board, order)

    def remove_board(self, query_manager, board: Board):
        return self._remove_element(query_manager, board)
