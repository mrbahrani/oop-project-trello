from .table import Table
from .user import User


class Board:
    def __init__(self):
        self.name = str()
        self.members = list()
        self.tables = list()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_table(self, table: Table):
        self.tables.append(table)

    def remove_table(self, table: Table):
        for index, table_item in enumerate(self.tables):
            if table_item.match_table(table):
                self.tables.pop(index)
                break

    def add_member(self, member: User):
        self.members.append(member)

    def remove_member(self, member: User):
        for index, member_item in enumerate(self.members):
            if member.match_user(member_item):
                self.members.pop(member_item)
                break

    def match_board(self, board):
        return self.name == board.name and \
               self.members == board.order and \
               self.tables == board.description

