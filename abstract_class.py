from db_interface import QueryHandler


class AbstractItem:
    def __init__(self):
        self.id = int()
        self._name = str()
        self._description = str()
        self._order = int()
        self._elements_list = list()
        self.members = list()
        self.model_class = None

    def __contains__(self, element):
        return element in self._elements_list

    def __eq__(self, other):
        return self.id == other.id

    def _add_element(self, element):
        self._elements_list.append(element)
        return self._elements_list

    def _remove_element(self, element):
        try:
            self._elements_list.remove(element)
        except ValueError:  # if element doesnt exist in elements_list
            return None
        return self._elements_list

    def _reorder_elements(self, element, index: int):
        pass

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

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        try:
            self.members.remove(member)
        except ValueError:  # if element doesnt exist in elements_list
            return None
        return self.members

    def _get_elements_list(self):
        return self._elements_list


