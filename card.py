class Card:
    def __init__(self):
        self.name = str()
        self.checkList = list()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addCheckListElement(self, checkListElement):
        self.checkList.append(checkListElement)

    def removeCheckListElement(self, card):
        for checkListElementIndex in len(self.checkListElement):
            if self.cards[checkListElementIndex].matchUser(card):
                self.cards.pop(checkListElementIndex)
