from lib.game import *

class UserInterface:
    def __init__(self, io, game, player):
        self.io = io
        self.game = game
        self.player = player

    def run(self, player_name):
        self._show(f"Welcome to the game {player_name}!")
        self._show("Set up your ships first.")
        while (len(self.game.remaining_ships)) > 0:
            self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message()))
            self._prompt_for_ship_placement()
            self._show("This is your board now:")
            self._show(self._format_board())
    def turn(self, player_name):
        '''show the moves so far'''
        self._show(f"It's your turn to shoot {player_name}!\n Here's your moves so far.")
        self._show(f"")

        self._show(f"Set up your ships first.")
        while (len(self.game.remaining_ships)) > 0:
            self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message()))
            self._prompt_for_ship_placement()
            self._show("This is your board now:")
            self._show(self._format_board())
        '''prompt for next move'''
        '''pass move into board'''
        '''return the hit or not'''
        '''show the board now'''

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.remaining_ships]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self):

        # these comments have logic to repeat prompts if there's non-accepted inputs in the program
        # while True:
        ship_length = self._prompt("Which do you wish to place?")
            # unplaced = self._ships_unplaced_message()
        #     if str(ship_length) in unplaced.split():
        #         break
        # while True:
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        #     if ship_orientation in ['v', 'h']:
        #         break
        # while True:    
        ship_row = self._prompt("Which row?")
        #     if int(ship_row) > 0 and int(ship_row)%1 == 0:
        #         break
        # while True:
        ship_col = self._prompt("Which column?")
            # if int(ship_col) > 0 and int(ship_col)%1==0:
            #     break
        self._show("OK.")
        outcome = self.game.place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
        )
        self._show(outcome)

    def _format_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)
    

