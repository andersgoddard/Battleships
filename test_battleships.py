import pytest
from battleships import *
from ocean import *
from space import *
from ships import *



def test_create_ocean():
    ocean = Ocean()
    assert ocean._width == 10
    assert ocean._height == 10
    assert ocean.get_char_at(3, 4) == '~'
    assert ocean.get_char_at(8, 8) == '~'
    
def test_create_and_hit_space():
    space1 = Space()
    assert space1.get_char_representation() == '~'
    successful_hit = True
    space1.take_shot(successful_hit)
    assert space1.get_char_representation() == 'X'

def test_hit_space_in_ocean():
    ocean = Ocean()
    ocean.take_shot(2, 3)
    assert ocean.get_char_at(2, 3) == 'X'
    
def test_set_space_at():
    ocean = Ocean()
    ocean.set_space_at(4, 5, Space())
    assert ocean.get_char_at(4, 5) == '~'
    
def test_create_ships():
    battleship1 = Battleship()
    assert battleship1.get_length() == 4
    assert battleship1.get_char_representation() == 'B'
    
    cruiser1 = Cruiser()
    assert cruiser1.get_length() == 3
    assert cruiser1.get_char_representation() == 'C'
    
    destroyer1 = Destroyer()
    assert destroyer1.get_length() == 2
    assert destroyer1.get_char_representation() == 'D'
    
    submarine1 = Submarine()
    assert submarine1.get_length() == 1
    assert submarine1.get_char_representation() == 'S'
   
def test_place_individual_ships():
    ocean = Ocean()
    battleship2 = Battleship()
    ocean.place_ship_at(1, 1, battleship2, horizontal=True)
    assert ocean.get_type_at(1, 1) == "Battleship"
    assert ocean.get_type_at(1, 2) == "Battleship"
    assert ocean.get_type_at(1, 3) == "Battleship"
    assert ocean.get_type_at(1, 4) == "Battleship"
    
    cruiser2 = Cruiser()
    ocean.place_ship_at(4, 4, cruiser2, horizontal=False)
    assert ocean.get_type_at(4, 4) == "Cruiser"
    assert ocean.get_type_at(5, 4) == "Cruiser"
    assert ocean.get_type_at(6, 4) == "Cruiser"
    assert ocean.get_char_at(7, 4) == '~'
    
def test_get_ship_positions():
    ocean = Ocean()
    battleship3 = Battleship()
    ocean.place_ship_at(2, 2, battleship3, horizontal=True)
    assert battleship3.get_ship_positions() == [(2, 2), (2, 3), (2, 4), (2, 5)]
    cruiser3 = Cruiser()
    ocean.place_ship_at(4, 4, cruiser3, horizontal=False)
    assert cruiser3.get_ship_positions() == [(4, 4), (5, 4), (6, 4)]
    
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
    
    battleship4 = Battleship()
    ocean.place_ship_at(2, 2, battleship4, horizontal=True)
    assert (ocean.is_open_position((2, 2))) == False
    assert (ocean.is_open_position((2, 3))) == False
    assert (ocean.is_open_position((2, 4))) == False
    assert (ocean.is_open_position((2, 5))) == False
    
    # assert (ocean.is_open_position((1, 1))) == False
        
    #check vertical example
    assert (ocean.is_open_position((4, 4))) == True
    assert (ocean.is_open_position((5, 4))) == True
    assert (ocean.is_open_position((6, 4))) == True
    
    #check diagonally adjacent spaces
    assert (ocean.is_open_position((3, 3))) == True
    assert (ocean.is_open_position((3, 5))) == True
    assert (ocean.is_open_position((7, 3))) == True
    assert (ocean.is_open_position((7, 5))) == True    
    
    cruiser4 = Cruiser()
    ocean.place_ship_at(4, 4, battleship4, horizontal=False)
    assert (ocean.is_open_position((4, 4))) == False
    assert (ocean.is_open_position((5, 4))) == False
    assert (ocean.is_open_position((6, 4))) == False
    
    
    
# def test_is_sunk():
    # s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    # assert is_sunk(s) == True
    # #add at least four more tests for is_sunk by the project submission deadline

# def test_ship_type():
    # #add at least one test for ship_type by the deadline of session 7 assignment
    # #provide at least five tests in total for ship_type by the project submission deadline
  

def test_is_open_sea():
    #add at least one test for open_sea by the deadline of session 7 assignment
    #provide at least five tests in total for open_sea by the project submission deadline
    ocean = Ocean()
    ocean.set_space_at(4, 5, Space())
    assert ocean.get_space_at(4, 5).is_open_sea() == True
    ocean.set_space_at(7, 7, Submarine())
    assert ocean.get_space_at(7, 7).is_open_sea() == False
    
# def test_ok_to_place_ship_at():
    # #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    # #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

# def test_place_ship_at():
    # #add at least one test for place_ship_at by the deadline of session 7 assignment
    # #provide at least five tests in total for place_ship_at by the project submission deadline

# def test_check_if_hits():
    # #add at least one test for check_if_hits by the deadline of session 7 assignment
    # #provide at least five tests in total for check_if_hits by the project submission deadline

# def test_hit():
    # #add at least one test for hit by the deadline of session 7 assignment
    # #provide at least five tests in total for hit by the project submission deadline

# def test_are_unsunk_ships_left():
    # #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    # #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
