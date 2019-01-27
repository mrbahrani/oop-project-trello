from models import *


db_map = {
    CardModel: ["name", "order", "description", "table"],
    CommentModel: ["text", "user", "card"],
    TableModel: ["name", "board"],
    BoardModel: ["name", "team"],
    TeamModel: ["name"],
    UserModel: ["name", "username", "email", "password"]
}

parents = ["table", "board", "team", "card"]
