from .user import User
from .board import Board


class Team:
    def __init__(self):
        self.name = str()
        self.description = str()
        self.members = list()
        self.boards = list()

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def add_member(self, member: User):
        self.members.append(member)

    def remove_member(self, member: User):
        for index, member_item in enumerate(self.members):
            if member.match_user(member_item):
                self.members.pop(member_item)
                break

    def add_board(self, board: Board):
        self.boards.append(board)

    def remove_board(self, board: Board):
        for index, board_item in enumerate(self.boards):
            if board.match_board(board_item):
                self.members.pop(board_item)
                break

    def match_team(self, team):
        pass
