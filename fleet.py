from ocean import *

class Fleet:
    def __init__(self):
        self._capacity = 10
        self.fleet = []
        
    def get_capacity(self):
        return self._capacity
        
    def get_current_size(self):
        return len(self.fleet)
        
    def add_ship(self, ship):
        self.fleet.append(ship)
        
    def get_fleet(self):
        return self.fleet
       