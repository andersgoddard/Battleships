class Ship:
    def get_length(self):
        return self._length
    
class Battleship(Ship):
    def __init__(self):
        self._length = 4
        
class Cruiser(Ship):
    def __init__(self):
        self._length = 3
        
class Destroyer(Ship):
    def __init__(self):
        self._length = 2
        
class Submarine(Ship):
    def __init__(self):
        self._length = 1