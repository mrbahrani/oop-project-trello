from card import Card

class Table:
    def __init__(self):
        self.name = str
        self.cards = list()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        for index, card_item in enumerate(self.cards):
            if card.match_card(card_item):
                self.cards.pop(index)
                break

    def move_card(self, card: Card, table, order):
        pass

    def reorder_card(self, card: Card, index):
        pass

    def match_table(self, table):
        pass
