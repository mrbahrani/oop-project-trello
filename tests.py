from board import Board
from team import Team
from user import User
from card import Card
from table import Table


def create_card(all_teams, query_manager):
    exec(open("./main.py").read())
    table = all_teams[0].boards[1].tables[3]
    c = Card()
    c.name = 'some name'
    c.description = 'dasdfsaf asdf asfg afg asdgawrgewqrg asdf'
    c.order = 121
    table.add_card(query_manager, c)


