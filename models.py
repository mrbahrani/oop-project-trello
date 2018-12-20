from peewee import *
import datetime
import random

db = SqliteDatabase('trello.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(default='')
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()


class Team(BaseModel):
    name = CharField()
    description = TextField(default='')


class Board(BaseModel):
    name = CharField()
    team = ForeignKeyField(Team, backref='boards')
    created_at = DateTimeField(default=datetime.datetime.now)


class Table(BaseModel):
    name = CharField()
    board = ForeignKeyField(Board, backref='tables')
    created_at = DateTimeField(default=datetime.datetime.now)


class Card(BaseModel):
    name = CharField()
    order = IntegerField()
    description = TextField(default='')
    table = ForeignKeyField(Table, backref='cards')
    created_at = DateTimeField(default=datetime.datetime.now)


class MemberRelation(BaseModel):
    member = ForeignKeyField(User, backref='memberships')
    card = ForeignKeyField(Card, backref='member_relations', null=False)
    board = ForeignKeyField(Board, backref='member_relations', null=False)
    team = ForeignKeyField(Team, backref='member_relations', null=False)


def initialize():
    db.connect()
    db.create_tables([User, Team, Board, Table, Card, MemberRelation], safe=True)
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
        u = User.create(
            name=user['name'],
            email=user['email'],
            username=user['username'],
            password=user['password'],
        )
        created_users.append(u)

    print(created_users)

    for team in teams:
        t = Team.create(
            name=team['name'],
            description=team['description']
        )


def add_some_tables():
    boards = Board.select()
    ts = []
    for i in range(30):
        t = Table.create(name='some table %d' % i,
                         board=boards[random.randrange(0, len(boards))])
        ts.append(t)
    print(ts)


def add_some_card():
    tables = Table.select()
    cs = []
    for table in tables:
        for i in range(random.randrange(5, 10)):
            c = Card.create(
                name='some card %d' % i,
                order=i,
                description='some looong loong description about what this card does or wants and whats needs to be done in order for this card to leave us the hell alone',
                table=table,
            )
            cs.append(c)

    print(cs)


def add_some_members():
    pass

def add_some_boards():
    teams = Team.select()
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
        b = Board.create(
            name=board['name'],
            team=teams[random.randrange(0, len(teams))]
        )
        bs.append(b)

    print(bs)


if __name__ == '__main__':
    initialize()
    # add_some_users_and_teams()
    # add_some_boards()
    # add_some_tables()
    # add_some_card()
