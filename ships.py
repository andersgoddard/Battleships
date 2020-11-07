from space import *  

# We represent a ship by means of tuples(row, column, horizontal, length, hits)

class Ship(Space):
    row = 0
    column = 0
    horizonal = None
    hits = 0

    def get_length(self):
        return self._length
        
    def is_open_sea(self):
        return False
        
    def get_ship_type(self):
        return self.ship_type

class Battleship(Ship):
    def __init__(self):
        self._length = 4
        self.char_representation = 'B'
        self.ship_type = "Battleship"        
        
class Cruiser(Ship):
    def __init__(self):
        self._length = 3
        self.char_representation = 'C'
        self.ship_type = "Cruiser"
        
class Destroyer(Ship):
    def __init__(self):
        self._length = 2
        self.char_representation = 'D'
        self.ship_type = "Destroyer"

class Submarine(Ship):
    def __init__(self):
        self._length = 1
        self.char_representation = 'S'
        self.ship_type = "Submarine"