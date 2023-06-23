class User():
    def __init__(self, game1, opponent, name):
        self.name = name
        self.own_game = game1
        self.opponent = opponent
        self.opponent_board = [
        '..........',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........']

            
    def shoot(self):
        board = '\n'.join(self.opponent_board)
        print (f"Here's what you've shot so far:\n {board}")
        row = input('Which row?')
        column = input('Which column?')
        board_row = list(self.opponent_board[row-1])
        if row not in range(self.own_game.rows) or column not in range(self.own_game.cols):
            return 'That\'s not on the board!'
        if self.opponent.ship_at(row,column):
            board_row[column-1] = 'X'
            self.opponent_board[row-1] = ''.join(board_row)
            current_status = 0
            for i in self.opponent.ships_placed:
                if (row, column) in i.coords:
                    i.status -= 1
                    current_status = i.status
            return 'Hit!' if current_status >= 1 else 'Hit! Ship destroyed!'
        else:
            board_row[column-1] = 'O'
            self.opponent_board[row-1] = ''.join(board_row)
            return 'Shot missed!'
    
    def is_game_over(self):
        hits_remaining = 0
        for i in self.opponent.ships_placed:
            hits_remaining += i.status
        return hits_remaining == 0