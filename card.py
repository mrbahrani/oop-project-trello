# from abstract_class import ComposedItem as AbstractItem
from abstract_class import ItemComponent as AbstractItem
from models import CardModel


class Card(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = CardModel
        self.comment_list = list()

    def add_comment(self, comment):
        self.comment_list.append(comment)

    def remove_comment(self, comment):
        for com in self.comment_list:
            if com.match(comment):
                self.comment_list.remove(com)
                break

        # self._elements_list = None  # card has no list of any sub-items

    # def add_check_list_element(self, checkListElement):
    #     self.checkList.append(checkListElement)

    # def remove_check_list_element(self, card):
    #     for checkListElementIndex in len(self.checkListElement):
    #         if self.cards[checkListElementIndex].matchUser(card):
    #             self.cards.pop(checkListElementIndex)
