from db_interface import QueryHandler


class AbstractItem:
    def __init__(self):
        self.id = None
        self.name = str()
        self.description = str()
        self.order = int()
        self._elements_list = list()
        self._members = list()
        self.model_class = None

    def __contains__(self, element):
        return element in self._elements_list

    def __eq__(self, other):
        return self.id == other.id

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def _add_element(self, query_manager, element, order=None):
        element = element.save(query_manager)
        if order:
            self._elements_list.insert(order, element)
        else:
            self._elements_list.append(element)
        return self._elements_list

    def _remove_element(self, query_manager, element):
        try:
            self._elements_list.remove(element)
            element.delete(query_manager)  # delete rom database
            del element  # delete the object itself
        except ValueError:  # if element doesnt exist in elements_list
            return None
        return self._elements_list

    def _reorder_elements(self, element, index: int):
        pass

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_order(self, order):
        self.order = order

    def get_order(self):
        return self.order

    def add_member(self, member):
        self._members.append(member)

    def remove_member(self, member):
        try:
            self._members.remove(member)
        except ValueError:  # if element doesnt exist in members
            return None
        return self._members

    def _get_elements_list(self):
        return self._elements_list

    def save(self, query_manager):
        if not self.id:  # if object has no instance in db then create it
            element = query_manager.create_object(self)
        else:  # if object already exists in db then update it
            element = query_manager.update_object(self)
        return element

    def delete(self, query_manager):
        #  if object is saved in db then delete it from db
        if self.id:
            query_manager.delete_object(self)
            self.id = None
