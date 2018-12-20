from peewee import *

db = SqliteDatabase('trello.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()


class Team(BaseModel):
    name = CharField()
    description = TextField()


class Board(BaseModel):
    name = CharField()
    team = ForeignKeyField(Team, backref='boards')


class Table(BaseModel):
    name = CharField()
    board = ForeignKeyField(Board, backref='tables')


class Card(BaseModel):
    name = CharField()
    order = IntegerField()
    description = TextField()
    table = ForeignKeyField(Table, backref='cards')


class MemberRelation(BaseModel):
    member = ForeignKeyField(User, backref='memberships')
    card = ForeignKeyField(Card, backref='member_relations')
    board = ForeignKeyField(Board, backref='member_relations')
    team = ForeignKeyField(Team, backref='member_relations')
