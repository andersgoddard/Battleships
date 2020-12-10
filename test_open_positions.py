import pytest
from battleships import *
from ocean import *
from space import *
from ships import *

def test_check_open_position():
    ocean = Ocean()
    
    #check horizontal example
    assert (ocean.is_open_position((2, 2))) == True
    assert (ocean.is_open_position((2, 3))) == True
    assert (ocean.is_open_position((2, 4))) == True
    assert (ocean.is_open_position((2, 5))) == True
    
    #check diagonally adjacent spaces
    assert (ocean.is_open_position((1, 1))) == True
    assert (ocean.is_open_position((1, 6))) == True
    assert (ocean.is_open_position((3, 1))) == True
    assert (ocean.is_open_position((3, 6))) == True
    
    #check spaces above and below
    assert (ocean.is_open_position((1, 2))) == True
    assert (ocean.is_open_position((1, 3))) == True
    assert (ocean.is_open_position((1, 4))) == True
    assert (ocean.is_open_position((1, 5))) == True
    assert (ocean.is_open_position((3, 2))) == True
    assert (ocean.is_open_position((3, 3))) == True
    assert (ocean.is_open_position((3, 4))) == True
    assert (ocean.is_open_position((3, 5))) == True
    
    #check spaces either side
    assert (ocean.is_open_position((2, 1))) == True
    assert (ocean.is_open_position((2, 6))) == True
    
    #check vertical example
    assert (ocean.is_open_position((4, 4))) == True
    assert (ocean.is_open_position((5, 4))) == True
    assert (ocean.is_open_position((6, 4))) == True
    
    #check diagonally adjacent spaces
    assert (ocean.is_open_position((3, 3))) == True
    assert (ocean.is_open_position((3, 5))) == True
    assert (ocean.is_open_position((7, 3))) == True
    assert (ocean.is_open_position((7, 5))) == True    
    
    #check spaces above and below
    assert (ocean.is_open_position((3, 4))) == True
    assert (ocean.is_open_position((7, 4))) == True
    
    #check spaces either side
    assert (ocean.is_open_position((4, 3))) == True
    assert (ocean.is_open_position((5, 3))) == True
    assert (ocean.is_open_position((6, 3))) == True
    assert (ocean.is_open_position((4, 5))) == True
    assert (ocean.is_open_position((5, 5))) == True
    assert (ocean.is_open_position((6, 5))) == True
    
    battleship4 = Battleship()
    ocean.place_ship_at(2, 2, battleship4, horizontal=True)
    assert (ocean.is_open_position((2, 2))) == False
    assert (ocean.is_open_position((2, 3))) == False
    assert (ocean.is_open_position((2, 4))) == False
    assert (ocean.is_open_position((2, 5))) == False
    
    cruiser4 = Cruiser()
    ocean.place_ship_at(4, 4, battleship4, horizontal=False)
    assert (ocean.is_open_position((4, 4))) == False
    assert (ocean.is_open_position((5, 4))) == False
    assert (ocean.is_open_position((6, 4))) == False
    
    #check horizontal example
    assert (ocean.is_open_position((2, 2))) == False
    assert (ocean.is_open_position((2, 3))) == False
    assert (ocean.is_open_position((2, 4))) == False
    assert (ocean.is_open_position((2, 5))) == False
    
    #check diagonally adjacent spaces
    assert (ocean.is_open_position((1, 1))) == False
    assert (ocean.is_open_position((1, 6))) == False
    assert (ocean.is_open_position((3, 1))) == False
    assert (ocean.is_open_position((3, 6))) == False
    
    #check spaces above and below
    assert (ocean.is_open_position((1, 2))) == False
    assert (ocean.is_open_position((1, 3))) == False
    assert (ocean.is_open_position((1, 4))) == False
    assert (ocean.is_open_position((1, 5))) == False
    assert (ocean.is_open_position((3, 2))) == False
    assert (ocean.is_open_position((3, 3))) == False
    assert (ocean.is_open_position((3, 4))) == False
    assert (ocean.is_open_position((3, 5))) == False
    
    #check spaces either side
    assert (ocean.is_open_position((2, 1))) == False
    assert (ocean.is_open_position((2, 6))) == False
    
    #check vertical example
    assert (ocean.is_open_position((4, 4))) == False
    assert (ocean.is_open_position((5, 4))) == False
    assert (ocean.is_open_position((6, 4))) == False
    
    #check diagonally adjacent spaces
    assert (ocean.is_open_position((3, 3))) == False
    assert (ocean.is_open_position((3, 5))) == False
    assert (ocean.is_open_position((7, 3))) == False
    assert (ocean.is_open_position((7, 5))) == False    
    
    #check spaces above and below
    assert (ocean.is_open_position((3, 4))) == False
    assert (ocean.is_open_position((7, 4))) == False
    
    #check spaces either side
    assert (ocean.is_open_position((4, 3))) == False
    assert (ocean.is_open_position((5, 3))) == False
    assert (ocean.is_open_position((6, 3))) == False
    assert (ocean.is_open_position((4, 5))) == False
    assert (ocean.is_open_position((5, 5))) == False
    assert (ocean.is_open_position((6, 5))) == False
    
    #check random empty space
    assert (ocean.is_open_position((8, 6))) == True

def test_edge_case_open_positions():
    ocean = Ocean()
    ocean.place_ship_at(0, 0, Battleship(), horizontal=True)
    assert (ocean.is_open_position((0, 0))) == False
    assert (ocean.is_open_position((0, 1))) == False
    assert (ocean.is_open_position((0, 2))) == False
    assert (ocean.is_open_position((0, 3))) == False
    assert (ocean.is_open_position((0, 4))) == False
    assert (ocean.is_open_position((1, 0))) == False
    assert (ocean.is_open_position((1, 1))) == False
    assert (ocean.is_open_position((1, 2))) == False
    assert (ocean.is_open_position((1, 3))) == False
    assert (ocean.is_open_position((1, 4))) == False
    assert (ocean.is_open_position((1, 5))) == True
    
def test_vlad_cases():
    ocean = Ocean()
    ocean.place_ship_at(2, 3, Cruiser(), horizontal=False)
    ocean.place_ship_at(6, 9, Battleship(), horizontal=False)
    assert (ocean.is_open_position((5, 7))) == True
    assert (ocean.is_open_position((5, 8))) == False # This passes here and in the first indicative test but is failing to recognise the destroyer starting at 5, 7 isn't valid...