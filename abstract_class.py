class AbstractItem:
    def __init__(self):
        self._name = str()
        self._description = str()
        self._order = int()

    def add_element(self, element, elements_list: list):
        elements_list.append(element)
        return elements_list

    def remove_element(self, element, elements_list: list):
        try:
            elements_list.remove(element)
        except ValueError:  # if element doesnt exist in elements_list
            return None
        return elements_list

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    def set_order(self, order):
        self._order = order

    def get_order(self):
        return self._order

    def reorder_elements(self, elements_list: list, element, index: int):
        pass
