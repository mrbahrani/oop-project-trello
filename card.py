class Card:
    def __init__(self):
        self.name = str()
        self.order = int()
        self.description = str()
        # self.checkList = list()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_order(self, order):
        self.order = order

    def get_order(self):
        return self.order

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def match_card(self, card):
        return self.name == card.name and \
               self.order == card.order and \
               self.description == card.description

    # def add_check_list_element(self, checkListElement):
    #     self.checkList.append(checkListElement)

    # def remove_check_list_element(self, card):
    #     for checkListElementIndex in len(self.checkListElement):
    #         if self.cards[checkListElementIndex].matchUser(card):
    #             self.cards.pop(checkListElementIndex)
