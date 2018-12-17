class Table:
    def __init__(self):
        self.name = str
        self.cards = list()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self, card):
        for cardIndex in len(self.cards):
            if self.cards[cardIndex].matchUser(card):
                self.cards.pop(cardIndex)

    def moveCard(self, card, table, order):
        pass

    def reorderCard(self, card, index):
        pass