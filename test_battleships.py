import pytest
from battleships import *
from ocean import *
from space import *
from ships import *

ocean = Ocean()

def test_create_ocean():
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
    ocean.take_shot(2, 3)
    assert ocean.get_char_at(2, 3) == 'X'
    
def test_set_space_at():
    ocean.set_space_at(4, 5)
    assert ocean.get_char_at(4, 5) == '~'
    
def test_create_ships():
    battleship = Battleship()
    assert battleship.get_length() == 4
    assert battleship.get_char_representation() == 'B'
    cruiser = Cruiser()
    assert cruiser.get_length() == 3
    assert cruiser.get_char_representation() == 'C'
    destroyer = Destroyer()
    assert destroyer.get_length() == 2
    assert destroyer.get_char_representation() == 'D'
    submarine = Submarine()
    assert submarine.get_length() == 1
    assert submarine.get_char_representation() == 'S'
   
# def test_is_sunk1():
    # s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    # assert is_sunk(s) == True
    # #add at least four more tests for is_sunk by the project submission deadline

# def test_ship_type1():
    # #add at least one test for ship_type by the deadline of session 7 assignment
    # #provide at least five tests in total for ship_type by the project submission deadline

# def test_is_open_sea1():
    # #add at least one test for open_sea by the deadline of session 7 assignment
    # #provide at least five tests in total for open_sea by the project submission deadline

# def test_ok_to_place_ship_at1():
    # #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    # #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

# def test_place_ship_at1():
    # #add at least one test for place_ship_at by the deadline of session 7 assignment
    # #provide at least five tests in total for place_ship_at by the project submission deadline

# def test_check_if_hits1():
    # #add at least one test for check_if_hits by the deadline of session 7 assignment
    # #provide at least five tests in total for check_if_hits by the project submission deadline

# def test_hit1():
    # #add at least one test for hit by the deadline of session 7 assignment
    # #provide at least five tests in total for hit by the project submission deadline

# def test_are_unsunk_ships_left1():
    # #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    # #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
