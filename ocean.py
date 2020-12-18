from space import *
from ships import *
from fleet import *
import random

class Ocean:   
    def __init__(self):
        self._width = 10
        self._height = 10
        self.ocean = []
        self.open_ocean_positions = []
        self.create_empty_ocean()
        
    def create_empty_ocean(self):
        for column in range(self._width):
            self.ocean.append([])
            for row in range(self._height):
                self.ocean[column].append(Space()) 
                position = (row, column)
                self.open_ocean_positions.append(position)    
                        
    def display_ocean(self):
        for i in range(self.get_width()):
          if i == 0: print(' ', end = " ")
          print(i, end = " ")
        print('\n')
    
        for i in range(self.get_width()):
            print(i, end = " ")
            for j in range(self.get_height()):
              print(self.get_char_at(i, j), end = " ")
            print('\n')
        
    def get_width(self):
        return self._width
        
    def get_height(self):
        return self._height
    
    def is_open_position(self, position):
        return (position in self.open_ocean_positions) 
       
    def is_open_sea(self, row, column):
        position = (row, column)
        return self.is_open_position(position)
    
    def set_space_at(self, row, column, space):
        self.ocean[row][column] = space
        
    def get_space_at(self, row, column):
        return self.ocean[row][column]
        
    def get_char_at(self, row, column):
        return self.get_space_at(row, column).get_char_representation()
        
    def get_type_at(self, row, column):
        return self.get_space_at(row, column).get_ship_type()
        
    def get_surrounding_positions(self, position):
        surrounding_positions = set()
        row = position[0]
        column = position[1]
        
        surrounding_positions.add((row-1, column-1))
        surrounding_positions.add((row-1, column))
        surrounding_positions.add((row-1, column+1))
        surrounding_positions.add((row, column-1))
        surrounding_positions.add((row, column))
        surrounding_positions.add((row, column+1))
        surrounding_positions.add((row+1, column-1))
        surrounding_positions.add((row+1, column))
        surrounding_positions.add((row+1, column+1))
        
        return surrounding_positions

    def take_shot(self, row, column):
        position = self.get_space_at(row, column)

        if position.get_type() == "Space":
            position.check_shot(position)
        elif position.get_type() == "Position":
            position.get_ship().check_shot(position)
            
    def get_closed_positions(self, row, column, ship, horizontal):
        resulting_closed_positions = set()
        for i in range(ship.get_length()):
            if horizontal:
                position = (row, column+i)
                ship.add_position(row, column+i)                
                self.set_space_at(row, column+i, ship.get_position(row, column+i))
            else:
                position = (row+i, column)
                ship.add_position(row+i, column)                
                self.set_space_at(row+i, column, ship.get_position(row+i, column))
            resulting_closed_positions.add(position)
            resulting_closed_positions = resulting_closed_positions.union(self.get_surrounding_positions(position))
        return resulting_closed_positions
        
    def remove_closed_positions(self, positions):
        for position in positions:
            if position in self.open_ocean_positions:
                self.open_ocean_positions.remove(position)
    
    def get_open_positions(self, ship=None, horizontal=-1):
        
        if horizontal == -1:
            return self.open_ocean_positions
                
        return_positions = self.open_ocean_positions[:]

        if horizontal:
            for position in self.open_ocean_positions:
                if (position[1] + ship.get_length()) > self._width:
                    return_positions.remove(position)
                else:
                    for i in range(ship.get_length()):
                        if ((position[0], position[1]+i) not in self.open_ocean_positions):
                            return_positions.remove(position)
                            break
        else:
            for position in self.open_ocean_positions:
                if (position[0] + ship.get_length()) > self._height:
                    return_positions.remove(position)
                else:
                    for i in range(ship.get_length()):
                        if ((position[0]+i, position[1]) not in self.open_ocean_positions):
                            return_positions.remove(position)
                            break
        
        return return_positions
    
    def place_ship_at(self, row, column, ship, horizontal):
        ship.set_horizontal_bool(horizontal)
        ship.set_starting_row(row)
        ship.set_starting_column(column)
        
        resulting_closed_positions = self.get_closed_positions(row, column, ship, horizontal)                    
        self.remove_closed_positions(list(resulting_closed_positions))
    
    def build_basic_fleet(self, fleet):
        for i in range(fleet.get_capacity()):
            if i < 1:
                ship = Battleship()
            elif i < 3:
                ship = Cruiser()
            elif i < 6:
                ship = Destroyer()
            else:
                ship = Submarine()
            open_positions = self.get_open_positions(ship, horizontal=True)
            row = open_positions[0][0]
            column = open_positions[0][1]
            self.place_ship_at(row, column, ship, horizontal=True)
            fleet.add_ship(ship)
            
    def build_random_fleet(self, fleet):
        orientation_choices = [True, False]
        for i in range(fleet.get_capacity()):
            if i < 1:
                ship = Battleship()
            elif i < 3:
                ship = Cruiser()
            elif i < 6:
                ship = Destroyer()
            else:
                ship = Submarine()
            horizontal = random.choice(orientation_choices)
            open_positions = self.get_open_positions(ship, horizontal)
            open_position = random.choice(open_positions)
            row = open_position[0]
            column = open_position[1]
            self.place_ship_at(row, column, ship, horizontal)
            fleet.add_ship(ship)            
                