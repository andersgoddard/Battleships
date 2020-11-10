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

def test_hit_space_in_ocean():
    ocean = Ocean()
    ocean.take_shot(2, 3)
    assert ocean.get_char_at(2, 3) == '.'
    
def test_set_space_at():
    ocean = Ocean()
    ocean.set_space_at(4, 5, Space())
    assert ocean.get_char_at(4, 5) == '~'

def test_create_ships():
    battleship = Battleship()
    assert battleship.get_length() == 4
    assert battleship.sunk_char_representation == 'B'
    
    cruiser1 = Cruiser()
    assert cruiser.get_length() == 3
    assert cruiser.sunk_char_representation == 'C'
    
    destroyer1 = Destroyer()
    assert destroyer.get_length() == 2
    assert destroyer.sunk_char_representation == 'D'
    
    submarine1 = Submarine()
    assert submarine.get_length() == 1
    assert submarine.sunk_char_representation == 'S'    
    
def test_place_individual_ships():
    ocean = Ocean()
    ocean.place_ship_at(1, 1, Battleship(), horizontal=True)
    assert ocean.get_type_at(1, 1) == "Battleship"
    assert ocean.get_type_at(1, 2) == "Battleship"
    assert ocean.get_type_at(1, 3) == "Battleship"
    assert ocean.get_type_at(1, 4) == "Battleship"
    
    ocean.place_ship_at(4, 4, Cruiser(), horizontal=False)
    assert ocean.get_type_at(4, 4) == "Cruiser"
    assert ocean.get_type_at(5, 4) == "Cruiser"
    assert ocean.get_type_at(6, 4) == "Cruiser"
    assert ocean.get_char_at(7, 4) == '~'
    
def test_ship_is_horizontal():
    ocean = Ocean()
    battleship = Battleship()
    ocean.place_ship_at(1, 1, battleship, horizontal=True)
    assert battleship.is_horizontal() == True
    cruiser = Cruiser()
    ocean.place_ship_at(4, 4, cruiser, horizontal=False)
    assert cruiser.is_horizontal() == False
    
def test_is_open_sea_method():
    ocean = Ocean()
    ocean.set_space_at(4, 5, Space())
    assert ocean.is_open_sea(4, 5) == True
    ocean.place_ship_at(7, 7, Submarine(), horizontal=True)
    assert ocean.is_open_sea(7, 7) == False
    assert ocean.is_open_sea(8, 8) == False
    assert ocean.is_open_sea(7, 8) == False         
        
def test_get_ship_positions():
    ocean = Ocean()
    battleship = Battleship()
    ocean.place_ship_at(2, 2, battleship, horizontal=True)
    assert battleship.get_ship_positions() == [(2, 2), (2, 3), (2, 4), (2, 5)]
    cruiser = Cruiser()
    ocean.place_ship_at(4, 4, cruiser, horizontal=False)
    assert cruiser.get_ship_positions() == [(4, 4), (5, 4), (6, 4)]
    
def test_get_starting_row_column():
    ocean = Ocean()
    battleship = Battleship()
    ocean.place_ship_at(2, 3, battleship, horizontal=True)
    assert battleship.get_starting_row() == 2
    assert battleship.get_starting_column() == 3
    
def test_hit_ship_in_ocean():
    ocean = Ocean()
    battleship = Battleship()
    assert ocean.get_char_at(3, 4) == '~' # unchecked
    ocean.place_ship_at(2, 3, battleship, horizontal=True)
    ocean.take_shot(2, 3) # hits
    assert battleship.get_hits() == [(2, 3)]
    ocean.take_shot(2, 4) # hits
    assert battleship.get_hits() == [(2, 3), (2, 4)]
    ocean.take_shot(3, 4) # misses
    assert battleship.get_hits() == [(2, 3), (2, 4)]
    assert ocean.get_char_at(3, 4) == '.' # checked and missed
    assert ocean.get_char_at(2, 4) == 'X' # checked and hit

def test_sink_ships():
    ocean = Ocean()
    ocean.place_ship_at(4, 4, Cruiser(), horizontal=False)
    assert ocean.get_char_at(4, 4) == '~'
    assert ocean.get_char_at(5, 4) == '~'
    assert ocean.get_char_at(6, 4) == '~'    
    ocean.take_shot(4, 4)
    assert ocean.get_char_at(4, 4) == 'X'
    ocean.take_shot(5, 4)
    assert ocean.get_char_at(4, 4) == 'X'
    assert ocean.get_char_at(5, 4) == 'X'
    ocean.take_shot(6, 4)
    assert ocean.get_char_at(4, 4) == 'C'
    assert ocean.get_char_at(5, 4) == 'C'
    assert ocean.get_char_at(5, 4) == 'C'
    
# def test_is_sunk():
    # s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    # assert is_sunk(s) == True
    # #add at least four more tests for is_sunk by the project submission deadline

# def test_ship_type():
    # #add at least one test for ship_type by the deadline of session 7 assignment
    # #provide at least five tests in total for ship_type by the project submission deadline
  
# def test_is_open_sea():
    # #add at least one test for open_sea by the deadline of session 7 assignment
    # #provide at least five tests in total for open_sea by the project submission deadline
 
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
    
