from space import *  

# We represent a ship by means of tuples(row, column, horizontal, length, hits)

class Ship(Space):   
    def __init__(self):
        self.positions = []
        self.hits = []
        self.horizontal = None
        self.starting_row = -1
        self.starting_column = -1

    def get_length(self):
        return self._length
        
    def is_open_sea(self):
        return False
        
    def get_ship_type(self):
        return self.ship_type
        
    def add_position(self, row, column):
        position = (row, column)
        self.positions.append(position)
        
    def get_ship_positions(self):
        return self.positions

    def set_horizontal_bool(self, horizontal):
        self.horizontal = horizontal
        
    def is_horizontal(self):
        return self.horizontal
        
    def set_starting_row(self, row):
        self.starting_row = row
        
    def get_starting_row(self):
        return self.starting_row
        
    def set_starting_column(self, column):
        self.starting_column = column
        
    def get_starting_column(self):
        return self.starting_column

class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self._length = 4
        self.char_representation = 'B'
        self.ship_type = "Battleship"        
        
class Cruiser(Ship):
    def __init__(self):
        super().__init__()
        self._length = 3
        self.char_representation = 'C'
        self.ship_type = "Cruiser"
        
class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self._length = 2
        self.char_representation = 'D'
        self.ship_type = "Destroyer"

class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self._length = 1
        self.char_representation = 'S'
        self.ship_type = "Submarine"