from space import *

class Ocean:
    def create_empty_ocean(self):
        for i in range(self._width):
            self.ocean.append([])
            for j in range(self._height):
                self.ocean[i].append(EmptySpace()) 
   
    def __init__(self):
        self._width = 10
        self._height = 10
        self.ocean = []
        self.create_empty_ocean()
        
    def get_char_at(self, x, y):
        return self.ocean[x][y].get_char_representation()