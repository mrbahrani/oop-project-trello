from peewee import *
import datetime
import random

db = SqliteDatabase('trello.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):
    name = CharField(default='')
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()


class TeamModel(BaseModel):
    name = CharField()
    description = TextField(default='')


class BoardModel(BaseModel):
    name = CharField()
    team = ForeignKeyField(TeamModel, backref='boards')
    created_at = DateTimeField(default=datetime.datetime.now)


class TableModel(BaseModel):
    name = CharField()
    board = ForeignKeyField(BoardModel, backref='tables')
    created_at = DateTimeField(default=datetime.datetime.now)


class CardModel(BaseModel):
    name = CharField()
    order = IntegerField()
    description = TextField(default='')
    table = ForeignKeyField(TableModel, backref='cards')
    created_at = DateTimeField(default=datetime.datetime.now)


class CommentModel(BaseModel):
    text = CharField()
    description = TextField(default='')
    card = ForeignKeyField(CardModel, backref='comments')
    user = ForeignKeyField(UserModel, backref='comments')

    created_at = DateTimeField(default=datetime.datetime.now)


class MemberCardRelation(BaseModel):
    member = ForeignKeyField(UserModel, backref='memberships')
    card = ForeignKeyField(CardModel, backref='member_relations', null=False)


class MemberBoardRelation(BaseModel):
    member = ForeignKeyField(UserModel, backref='memberships')
    board = ForeignKeyField(BoardModel, backref='member_relations', null=False)


class MemberTeamRelation(BaseModel):
    member = ForeignKeyField(UserModel, backref='memberships')
    team = ForeignKeyField(TeamModel, backref='member_relations', null=False)


def initialize():
    db.connect()
    db.create_tables([UserModel, TeamModel, BoardModel, TableModel, CardModel, CommentModel,
                      MemberCardRelation, MemberBoardRelation, MemberTeamRelation], safe=True)
    # db.close()


def add_some_users_and_teams():
    users = [
        {'name': 'gholam', 'email': 'a@b.com', 'username': 'gholiGhollak', 'password': '123qweasd'},
        {'name': 'sheykh pashmeddin', 'email': 'aa@b.com', 'username': 'furryPashmak', 'password': 'asdfqwer'},
        {'name': 'sirish sefat', 'email': 'a@db.com', 'username': 'sooriSirish', 'password': 'erydfgh'},
        {'name': 'ghelghelak mirza', 'email': 'aadf@b.com', 'username': 'ghelGheli', 'password': 'xcvbsdfg'},
        {'name': 'ververe jadoo', 'email': 'a@sfb.com', 'username': 'veriVerVere', 'password': '1qaz2wsx'},
        {'name': 'kopol chorool', 'email': 'aasdf@basf.com', 'username': 'golabiPorHajm', 'password': 'edcrfv'},
        {'name': 'pakhmak-o-ddole', 'email': 'aasdf@bsdg.com', 'username': 'sidneySweet', 'password': 'tgbyhn'},
        {'name': 'mashangak', 'email': 'asdg@sdfb.com', 'username': 'stupidMashang', 'password': 'ujmik,'},
    ]
    teams = [
        {'name': 'the-A-team',
         'description': 'a team that actually does nothing and just about exist which constantly make idiot conversations'},
        {'name': 'translators',
         'description': 'some people saying none-sense jubarish in other languages witch means abso-bloody-lutely nothing'},
    ]
    created_users = []
    for user in users:
        u = UserModel.create(
            name=user['name'],
            email=user['email'],
            username=user['username'],
            password=user['password'],
        )
        created_users.append(u)

    print(created_users)

    for team in teams:
        t = TeamModel.create(
            name=team['name'],
            description=team['description']
        )


def add_some_tables():
    boards = BoardModel.select()
    ts = []
    for i in range(30):
        t = TableModel.create(name='some table %d' % i,
                         board=boards[random.randrange(0, len(boards))])
        ts.append(t)
    print(ts)


def add_some_card():
    tables = TableModel.select()
    cs = []
    for table in tables:
        for i in range(random.randrange(5, 10)):
            c = CardModel.create(
                name='some card %d' % i,
                order=i,
                description='some looong loong description about what this card does or wants and whats needs to be done in order for this card to leave us the hell alone',
                table=table,
            )
            cs.append(c)

    print(cs)


def add_some_comments():
    cards = CardModel.select()
    users = UserModel.select()
    cs = []
    for card in cards:
        for i in range(random.randrange(1, 5)):
            user = random.randrange(1, len(users))
            c = CommentModel.create(
                user=user,
                text='some text and comment that user {} wrote on this card'.format(user),
                card=card,
            )
            cs.append(c)

    print(cs)


def add_some_members():
    pass


def add_some_boards():
    teams = TeamModel.select()
    boards = [
        {'name': 'product backlog', 'team': ''},
        {'name': 'technical team', 'team': ''},
        {'name': 'lets do some tasks', 'team': ''},
        {'name': 'lets do nothing', 'team': ''},
        {'name': 'some useless board', 'team': ''},
        {'name': 'some cool board', 'team': ''},
        {'name': 'a board full of stars', 'team': ''},
    ]
    bs = []
    for board in boards:
        b = BoardModel.create(
            name=board['name'],
            team=teams[random.randrange(0, len(teams))]
        )
        bs.append(b)

    print(bs)


if __name__ == '__main__':
    initialize()
    add_some_users_and_teams()
    add_some_boards()
    add_some_tables()
    add_some_card()
    add_some_comments()
