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
        """

        :param query_manager:
        :param element:
        :param order:
        :return elements_list:

        this method saves passed `element` and adds it to elements list
        """
        order = order if order else len(self._elements_list)
        element.set_order(order)
        element_model = element.save(query_manager, self)
        element.set_id(element_model.id)
        self._elements_list.insert(order, element)
        self._reorder_elements(element, order)
        return self._elements_list

    def _remove_element(self, query_manager, element):
        """

        :param query_manager:
        :param element:
        :return:

        this method removes passed element both from database and elements list
        """
        try:
            self._elements_list.remove(element)
            element.delete(query_manager)  # delete rom database
            del element  # delete the object itself
        except ValueError:  # if element doesnt exist in elements_list
            return None
        return self._elements_list

    def _move_element(self, query_manager, element, parent_element, order=None):
        self._remove_element(query_manager, element)
        parent_element._add_element(query_manager, element, order)

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

    def save(self, query_manager, parent_element=None):
        """

        :param query_manager:
        :param parent_element:
        :return element:

        this method saves changes in this object
        updates if already exists in database
        or creates if its not in database
        """
        if not self.id:  # if object has no instance in db then create it
            if parent_element:
                print(parent_element)
                element = query_manager.create_object(self, parent_element)
            else:
                element = query_manager.create_object(self)
        else:  # if object already exists in db then update it
            element = query_manager.update_object(self)

        return element

    def delete(self, query_manager):
        """

        :param query_manager:
        :return:

        this method deletes current object from database
        """
        #  if object is saved in db then delete it from db
        if self.id:
            query_manager.delete_object(self)
            self.id = None
