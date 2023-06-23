import sys
from lib.game import Game
from lib.user_interface import UserInterface
from lib.user import *




class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)


io = TerminalIO()
game1 = Game()
game2 = Game()
player1 = User(game1, None, 'Sam')
player2 = User(game2, None, 'Lee')

game_over = False
p1_setup = False
p2_setup = False
player1.opponent = player2
player2.opponent = player1
user_interface_1 = UserInterface(io, game1, player1)
while p1_setup == False:
    user_interface_1.run('player 1')
    if game1.remaining_ships == []:
        p1_setup = True

user_interface_2 = UserInterface(io, game2, player2)
while p2_setup == False:
    user_interface_2.run('player 2')
    if game2.remaining_ships == []:
        p2_setup = True

current_player = player1

while game_over == False:
    current_player.shoot()
    if current_player.is_game_over():
        game_over = True
        print (f'{current_player.name} wins!')
    else:
        if current_player == player1:
            current_player == player2
        else:
            current_player = player1
        

