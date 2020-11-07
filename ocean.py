from space import *

class Ocean:
    def create_empty_ocean(self):
        for i in range(self._width):
            self.ocean.append([])
            for j in range(self._height):
                self.ocean[i].append(Space()) 
   
    def __init__(self):
        self._width = 10
        self._height = 10
        self.ocean = []
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