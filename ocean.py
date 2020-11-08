from space import *

class Ocean:
    def create_empty_ocean(self):
        for i in range(self._width):
            self.ocean.append([])
            for j in range(self._height):
                self.ocean[i].append(Space()) 
                position = (j, i)
                self.open_ocean_positions.append(position)
   
    def __init__(self):
        self._width = 10
        self._height = 10
        self.ocean = []
        self.open_ocean_positions = []
        self.create_empty_ocean()
        
    def set_space_at(self, row, column, space):
        self.ocean[row][column] = space
        
    def get_space_at(self, row, column):
        return self.ocean[row][column]
        
    def get_char_at(self, row, column):
        return self.get_space_at(row, column).get_char_representation()
        
    def take_shot(self, row, column):
        successful_hit = True
        self.get_space_at(row, column).take_shot(successful_hit)
        
    def place_ship_at(self, row, column, ship, horizontal):
        for i in range(ship.get_length()):
            if horizontal:
                position = (row, column+i)
                self.set_space_at(row, column+i, ship)
                ship.add_position(row, column+i)
            else:
                position = (row+i, column)
                self.set_space_at(row+i, column, ship)
                ship.add_position(row+i, column)
            if position in self.open_ocean_positions:
                self.open_ocean_positions.remove(position)
        
    def get_type_at(self, row, column):
        return self.get_space_at(row, column).get_ship_type()
        
    def is_open_position(self, position):
        return (position in self.open_ocean_positions)