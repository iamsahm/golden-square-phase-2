class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        self.status = length
        self.coords = []
        if orientation == 'vertical':
            for i in range(length):
                self.coords.append((row+i-1,col))
        if orientation == 'horizontal':
            for i in range(length):
                self.coords.append((row, col+i-1))

    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
