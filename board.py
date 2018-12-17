class Board:
    def __init__(self):
        self.name = str()
        self.members = list()
        self.tables = list()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addTable(self, table):
        self.tables.append(table)

    def removeTable(self, table):
        for tableIndex in len(self.table):
            if self.tables[tableIndex].matchBoard(table):
                self.tables.pop(tableIndex)

    def addMember(self, member):
        self.members.append(member)

    def removeMember(self, member):
        for memberIndex in len(self.members):
            if self.members[memberIndex].matchUser(member):
                self.members.pop(memberIndex)
