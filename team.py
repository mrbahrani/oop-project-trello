from user import User
from board import Board
from abstract_class import AbstractItem
from models import TeamModel


class Team(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = TeamModel

    @property
    def boards(self):
        return self._get_elements_list()

    def add_board(self, board: Board):
        return self._remove_element(board)

    def remove_board(self, board: Board):
        return self._remove_element(board)
