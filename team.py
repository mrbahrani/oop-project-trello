class Team:
    def __init__(self):
        self.name = str()
        self.description = str()
        self.members = list()
        self.boards = list()



    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def addMember(self, member):
        self.members.append(member)

    def removeMember(self, member):
        for memberIndex in len(self.members):
            if self.members[memberIndex].matchUser(member):
                self.members.pop(memberIndex)

    def addBoard(self, board):
        self.boards.append(board)

    def removeBoard(self, board):
        for boardIndex in len(self.boards):
            if self.boards[boardIndex].matchBoard(board):
                self.boards.pop(boardIndex)

    def matchTeam(self, teamTwo):
        pass




