from models import *
from board import Board
from table import Table
from card import Card
from user import User
from team import Team
from comment import Comment
from db_interface import QueryHandler


def load_db():
    teams = TeamModel.select()
    boards = BoardModel.select()
    tables = TableModel.select()
    cards = CardModel.select()
    users = UserModel.select()
    comments = CommentModel.select()
    return teams, boards, tables, cards, users, comments


def convert_to_user_classes(users):
    all_users = []
    for user in users:
        u = User()
        u.id = user.id
        u.set_name(user.name)
        u.set_username(user.username)
        u.set_email(user.email)
        u.set_name(user.name)
        u.set_password(user.password)
        all_users.append(u)
    return all_users


def convert_to_card_classes(cards, card_to_comments):
    all_cards = []
    table_to_card_map = dict()
    for card in cards:
        c = Card()
        c.set_id(card.id)
        c.set_description(card.description)
        c.set_order(card.order)
        c.set_name(card.name)
        c._elements_list = card_to_comments.get(c.get_id())

        if not table_to_card_map.get(card.table.id):
            table_to_card_map[card.table.id] = [c]
        else:
            table_to_card_map[card.table.id].append(c)

        all_cards.append(c)
    return all_cards, table_to_card_map


def convert_to_comment_classes(comments):
    all_comments = []
    card_to_comment_map = dict()
    for comment in comments:
        c = Comment()
        c.set_id(comment.id)
        c.set_text(comment.text)
        c.set_user(comment.user)

        if not card_to_comment_map.get(comment.card.id):
            card_to_comment_map[comment.card.id] = [c]
        else:
            card_to_comment_map[comment.card.id].append(c)

            all_comments.append(c)
    return all_comments, card_to_comment_map


def convert_to_table_classes(tables, table_to_card_map):
    all_items = []
    board_to_table = dict()
    for model in tables:
        item = Table()
        item.set_id(model.id)
        # item.set_description(model.description)
        # item.set_order(model.order)
        item.set_name(model.name)
        item._elements_list = table_to_card_map[item.get_id()]

        if not board_to_table.get(model.board.id):
            board_to_table[model.board.id] = [item]
        else:
            board_to_table[model.board.id].append(item)

        all_items.append(item)
    return all_items, board_to_table


def convert_to_board_classes(boards, board_to_table):
    all_items = []
    team_to_board = dict()
    for model in boards:
        item = Board()
        item.set_id(model.id)
        # item.set_description(model.description)
        # item.set_order(model.order)
        item.set_name(model.name)
        item._elements_list = board_to_table[item.get_id()]

        if not team_to_board.get(model.team.id):
            team_to_board[model.team.id] = [item]
        else:
            team_to_board[model.team.id].append(item)

        all_items.append(item)
    return all_items, team_to_board


def convert_to_team_classes(teams, team_to_board):
    all_items = []
    for model in teams:
        item = Team()
        item.set_id(model.id)
        item.set_description(model.description)
        # item.set_order(model.order)
        item.set_name(model.name)
        item._elements_list = team_to_board[item.get_id()]
        all_items.append(item)
    return all_items


def refresh_from_db():
    teams, boards, tables, cards, users, comments = load_db()
    all_users = convert_to_user_classes(users)
    all_comments, card_to_comments = convert_to_comment_classes(comments)
    all_cards, table_to_cards = convert_to_card_classes(cards, card_to_comments)
    all_tables, board_to_table = convert_to_table_classes(tables, table_to_cards)
    all_boards, team_to_board = convert_to_board_classes(boards, board_to_table)
    all_teams = convert_to_team_classes(teams, team_to_board)

    query_manager = QueryHandler()
    return all_comments, all_cards, all_users, all_boards, all_tables, all_teams, query_manager


if __name__ == "__main__":
    all_comments, all_cards, all_users, all_boards, all_tables, all_teams, qm = refresh_from_db()
