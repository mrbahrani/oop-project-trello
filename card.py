from abstract_class import AbstractItem
from models import CardModel


class Card(AbstractItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_class = CardModel

    # def add_check_list_element(self, checkListElement):
    #     self.checkList.append(checkListElement)

    # def remove_check_list_element(self, card):
    #     for checkListElementIndex in len(self.checkListElement):
    #         if self.cards[checkListElementIndex].matchUser(card):
    #             self.cards.pop(checkListElementIndex)
