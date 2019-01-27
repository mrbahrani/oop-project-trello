# from board import Board
# from team import Team
# from user import User
# from card import Card
# from table import Table
from main import *

all_comments, all_cards, all_users, all_boards, all_tables, all_teams, qm = refresh_from_db()

import unittest


class TestSum(unittest.TestCase):

    # def test_copy_element(self):
    #     c = all_tables[0].cards[0]
    #     all_tables[0].copy_card(qm, c, all_tables[1])
    #     self.assertTrue(c in all_tables[1])

    def test_add_comment(self):
        c = Comment()
        c.set_user(all_users[0].id)
        c.set_text('this is a comment by user {}'.format(all_users[0].id))
        # c = c.save(qm, all_cards[0])
        all_cards[0].add_comment(qm, c)
        self.assertTrue(c in all_cards[0])

    def test_remove_comment(self):
        c = all_cards[0].comments[0]
        all_cards[0].remove_comment(qm, c)
        self.assertFalse(c in all_cards[0])


if __name__ == '__main__':
    unittest.main()
