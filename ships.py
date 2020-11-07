from space import *  

class Ship(Space):
    def get_length(self):
        return self._length
        
    def is_open_sea(self):
        return False

class Battleship(Ship):
    def __init__(self):
        self._length = 4
        self.char_representation = 'B'
        
class Cruiser(Ship):
    def __init__(self):
        self._length = 3
        self.char_representation = 'C'
        
class Destroyer(Ship):
    def __init__(self):
        self._length = 2
        self.char_representation = 'D'

class Submarine(Ship):
    def __init__(self):
        self._length = 1
        self.char_representation = 'S'
        