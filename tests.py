import board
import team
import user
import card
import table


user_1 = user.User()
user_1.set_name('gholam')
user_1.set_email('a@a.b')
user_1.set_username('ghollak_pasand')

card_1 = card.Card()
card_1.set_name('do some task')
card_1.set_order(0)

table_1 = table.Table()
table_1.set_name('to do')
table_1.add_card(card_1)

board_1 = board.Board()
board_1.set_name('foo board')
board_1.add_table(table_1)


a_team = team.Team()
a_team.set_name('the a team')
a_team.add_board(board_1)
a_team.add_member(user_1)

print(a_team)