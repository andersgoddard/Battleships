from ocean import *

class Fleet:
    def __init__(self):
        self._capacity = 10
        self.fleet = []
        self.fleet_positions = []
        
    def get_capacity(self):
        return self._capacity
        
    def get_current_size(self):
        return len(self.fleet)
        
    def add_ship(self, ship):
        self.fleet.append(ship)
        for position in ship.get_positions():
            self.fleet_positions.append(position.get_position())
        
    def get_fleet(self):
        return self.fleet
        
    def get_fleet_positions(self):
        return self.get_fleet_positions
