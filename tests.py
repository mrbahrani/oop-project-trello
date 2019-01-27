# from board import Board
# from team import Team
# from user import User
# from card import Card
# from table import Table
from main import *
import unittest
import random

all_comments, all_cards, all_users, all_boards, all_tables, all_teams, qm = refresh_from_db()


class TestSum(unittest.TestCase):

    def test_copy_element(self):
        c = all_tables[0].cards[0]
        all_tables[0].copy_card(qm, c, all_tables[1])
        self.assertTrue(c in all_tables[1])

    def test_reorder_element(self):
        card = all_tables[3].cards[2]
        order = 4
        all_tables[3].reorder_cards(qm, card, order)
        for i, c in enumerate(all_tables[3].cards):
            if c == card:
                self.assertEqual(c.get_order(), order)
            self.assertEqual(c.get_order(), i)

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

    def test_members(self):
        test_cycles = 40
        test_card = None
        test_member = None
        test_index = random.randrange(0, test_cycles)
        for i in range(test_cycles):
            user = random.choice(all_users)
            card = random.choice(all_cards)
            card.members.add_member(user)
            if i == test_index:
                test_card = card
                test_member = user

        self.assertIn(test_member, test_card.members)

        test_card.members.remove_member(test_member)

        self.assertNotIn(test_member, test_card.members)



if __name__ == '__main__':
    unittest.main()
