from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.ships_placed = []
        self.rows = rows
        self.cols = cols
        self.remaining_ships = [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]

    def unplaced_ships(self):
        return self.remaining_ships()
    
            
    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
    
    
    def place_ship(self, length, orientation, row, col):
        try:
            ship_placement = ShipPlacement(
                length=length,
                orientation=orientation,
                row=row,
                col=col,
            )
            remaining_lengths =[x.length for x in self.remaining_ships]
            if length not in remaining_lengths:
                raise Exception('You\'ve got no ships with that length left!')
            ship_coords = []
            if orientation == 'vertical':
                for i in range(length):
                    ship_coords.append((row+i, col))
            else:
                for i in range(length):
                    ship_coords.append((row, col+i))

            for i in ship_coords:
                if self.ship_at(i[0],i[1]):
                    raise Exception('There\'s already a ship there! Try again.')    
            if int(row) < 1 or int(col) < 1 or int(row) + int(length) - 1 > self.rows and orientation == 'vertical' or int(col) + int(length) - 1 > self.cols and orientation == 'horizontal':
                raise Exception('Your ship won\'t fit there! Try again.')
            self.ships_placed.append(ship_placement)
            for i in self.remaining_ships:
                if i.length == length:
                    self.remaining_ships.pop(self.remaining_ships.index(i))
                    break
            return 'Ship placed!'
        except Exception as e:
                return str(e)