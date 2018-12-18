class Board:
    def __init__(self):
        self.name = str()
        self.members = list()
        self.tables = list()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_table(self, table):
        self.tables.append(table)

    def remove_table(self, table):
        for index, table_item in enumerate(self.tables):
            if table_item.matchBoard(table):
                self.tables.pop(index)
                break

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        for index, member_item in enumerate(self.members):
            if member.matchUser(member_item):
                self.members.pop(member_item)
                break

