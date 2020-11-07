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
        
    def get_char_at(self, row, column):
        return self.ocean[row][column].get_char_representation()
        
    def set_space_at(self, row, column):
        self.ocean[row][column] = Space()