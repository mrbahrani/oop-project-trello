from user import User
from board import Board
from abstract_class import ComposedItem
from models import TeamModel


class Team(ComposedItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = TeamModel

    @property
    def boards(self):
        return self._get_elements_list()

    def add_board(self, query_manager, board: Board, order=None):
        return self.add_element(query_manager, board, order)

    def remove_board(self, query_manager, board: Board):
        return self._remove_element(query_manager, board)

    def reorder_boards(self, query_manager, element=None, index=None):
        return self._reorder_elements(query_manager, element, index)
