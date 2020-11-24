from space import *
from fleet import *

# We represent a ship by means of tuples(row, column, horizontal, length, hits)

class Ship():   
    def __init__(self):
        super().__init__()
        self.positions = []
        self.position_tuples = []
        self.hits = set()
        self.horizontal = None
        self.starting_row = -1
        self.starting_column = -1

    def get_length(self):
        return self._length
        
    def get_ship_type(self):
        return self.ship_type

    def set_starting_row(self, row):
        self.starting_row = row
        
    def get_starting_row(self):
        return self.starting_row
        
    def set_starting_column(self, column):
        self.starting_column = column
        
    def get_starting_column(self):
        return self.starting_column
    
    def get_ship_positions(self):
        return self.position_tuples

    def set_hits(self, hits):
        self.hits = hits
    
    def get_hits(self):
        return self.hits
    
    def add_position(self, row, column):
        position = Position(row, column, self)
        self.position_tuples.append(position.get_position())
        self.positions.append(position)
        
    def get_position(self, row, column):
        position_index = self.position_tuples.index((row, column))
        return self.positions[position_index]

    def set_horizontal_bool(self, horizontal):
        self.horizontal = horizontal
        
    def get_horizontal_bool(self):
        return self.horizontal
                
    def is_horizontal(self):
        return self.horizontal
               
    def check_shot(self, position):
        position.set_is_checked(True)
        self.hits.add(position.get_position())
            
    def is_sunk(self):
        return len(self.get_hits()) >= self.get_length()

    def get_char_representation(self):
        return self.sunk_char_representation
        
    def get_type(self):
        return self.ship_type
        
    def get_game_representation(self):
        game_representation = (self.starting_row, self.starting_column, self.horizontal, self._length, self.hits)
        return game_representation

class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self._length = 4
        self.sunk_char_representation = 'B'
        self.ship_type = "Battleship"        
        
class Cruiser(Ship):
    def __init__(self):
        super().__init__()
        self._length = 3
        self.sunk_char_representation = 'C'
        self.ship_type = "Cruiser"
        
class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self._length = 2
        self.sunk_char_representation = 'D'
        self.ship_type = "Destroyer"

class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self._length = 1
        self.sunk_char_representation = 'S'
        self.ship_type = "Submarine"