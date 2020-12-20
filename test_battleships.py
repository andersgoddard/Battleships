import pytest
from battleships import *
from ocean import *
from space import *
from ships import *
from fleet import *

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
    
    cruiser = Cruiser()
    assert cruiser.get_length() == 3
    assert cruiser.sunk_char_representation == 'C'
    
    destroyer = Destroyer()
    assert destroyer.get_length() == 2
    assert destroyer.sunk_char_representation == 'D'
    
    submarine = Submarine()
    assert submarine.get_length() == 1
    assert submarine.sunk_char_representation == 'S'    
    
def test_get_char_at_position():
    ship = Battleship()
    position = Position(0,0, ship)
    position.get_char_representation = '~'

def test_get_open_positions():
    ocean = Ocean()
    assert ((6, 7) in ocean.get_open_positions()) == True # won't be open to a horizontal battleship
    assert ((7, 5) in ocean.get_open_positions()) == True # won't be open to a vertical battleship
    
    battleship = Battleship()
    assert((6, 7) in ocean.get_open_positions(battleship, horizontal=True)) == False
    assert((7, 5) in ocean.get_open_positions(battleship, horizontal=False)) == False
    assert((9, 3) in ocean.get_open_positions(battleship, horizontal=True)) == True
    assert((3, 9) in ocean.get_open_positions(battleship, horizontal=False)) == True
    
    destroyer = Destroyer()
    assert((6, 7) in ocean.get_open_positions(destroyer, horizontal=True)) == True
    assert((7, 5) in ocean.get_open_positions(destroyer, horizontal=False)) == True
    assert((9, 9) in ocean.get_open_positions(destroyer, horizontal=False)) == False
    
    submarine = Submarine()
    assert((9, 9) in ocean.get_open_positions(submarine, horizontal=True)) == True
    
def test_place_individual_ships():
    ocean = Ocean()
    ocean.place_ship_at(1, 1, Battleship(), horizontal=True)
    assert ocean.get_type_at(1, 1) == "battleship"
    assert ocean.get_type_at(1, 2) == "battleship"
    assert ocean.get_type_at(1, 3) == "battleship"
    assert ocean.get_type_at(1, 4) == "battleship"
    
    ocean.place_ship_at(4, 4, Cruiser(), horizontal=False)
    assert ocean.get_type_at(4, 4) == "cruiser"
    assert ocean.get_type_at(5, 4) == "cruiser"
    assert ocean.get_type_at(6, 4) == "cruiser"
    assert ocean.get_char_at(7, 4) == '~'
    
def test_ship_is_horizontal():
    ocean = Ocean()
    battleship = Battleship()
    ocean.place_ship_at(1, 1, battleship, horizontal=True)
    assert battleship.is_horizontal() == True
    cruiser = Cruiser()
    ocean.place_ship_at(4, 4, cruiser, horizontal=False)
    assert cruiser.is_horizontal() == False
    
def test_set_hits():
    ship = Battleship()
    assert ship.get_hits() == set()
    ship.set_hits({(2, 3)})
    assert ship.get_hits() == {(2, 3)}
    
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
    
def test_create_fleet():
    fleet = Fleet()
    assert fleet.get_capacity() == 10
    assert fleet.get_current_size() == 0    
    battleship = Battleship()
    fleet.add_ship(battleship)
    assert fleet.get_current_size() == 1    

def test_build_fleet():
    ocean = Ocean()
    fleet = Fleet()
    ocean.build_basic_fleet(fleet)
        
    assert fleet.get_fleet()[0].get_ship_positions() == [(0,0),(0,1),(0,2),(0,3)]
    assert fleet.get_fleet()[1].get_ship_positions() == [(2,0),(2,1),(2,2)]
    assert fleet.get_fleet()[2].get_ship_positions() == [(4,0),(4,1),(4,2)]
    assert fleet.get_fleet()[3].get_ship_positions() == [(6,0),(6,1)]
    assert fleet.get_fleet()[4].get_ship_positions() == [(8,0),(8,1)]
    assert fleet.get_fleet()[5].get_ship_positions() == [(6,3),(6,4)]
    assert fleet.get_fleet()[6].get_ship_positions() == [(8,3)]
    assert fleet.get_fleet()[7].get_ship_positions() == [(2,4)]
    assert fleet.get_fleet()[8].get_ship_positions() == [(4,4)]
    assert fleet.get_fleet()[9].get_ship_positions() == [(0,5)]

def test_hit_ship_in_ocean():
    ocean = Ocean()
    battleship = Battleship()
    assert ocean.get_char_at(3, 4) == '~' # unchecked
    ocean.place_ship_at(2, 3, battleship, horizontal=True)
    ocean.take_shot(2, 3) # hits
    assert battleship.get_hits() == {(2, 3)}
    ocean.take_shot(2, 4) # hits
    assert battleship.get_hits() == {(2, 3), (2, 4)}
    ocean.take_shot(3, 4) # misses
    assert battleship.get_hits() == {(2, 3), (2, 4)}
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
    assert ocean.get_char_at(5, 4) == '~'
    assert ocean.get_char_at(6, 4) == '~'    
    ocean.take_shot(5, 4)
    assert ocean.get_char_at(4, 4) == 'X'
    assert ocean.get_char_at(5, 4) == 'X'
    assert ocean.get_char_at(6, 4) == '~'    
    ocean.take_shot(6, 4)
    assert ocean.get_char_at(4, 4) == 'C'
    assert ocean.get_char_at(5, 4) == 'C'
    assert ocean.get_char_at(6, 4) == 'C'
    
def test_game_representations():
    ocean = Ocean()
    ship = Cruiser()
    ocean.place_ship_at(2, 3, ship, horizontal=False)
    ocean.take_shot(2, 3)
    ocean.take_shot(3, 3)
    ocean.take_shot(4, 3)
    assert ship.get_game_representation() == (2, 3, False, 3, {(2, 3),(3, 3),(4, 3)})   
    
def test_is_sunk():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    
    #add at least four more tests for is_sunk by the project submission deadline
    s2 = (9, 9, True, 1, set())
    assert is_sunk(s2) == False
    
    s3 = (0, 0, True, 4, {(0,0), (0,1), (0,2), (0,3)})
    assert is_sunk(s3) == True
    
    s4 = (8, 8, False, 2, {(8,8)})
    assert is_sunk(s4) == False

    s5 = (2, 3, False, 3, {(2,3), (3,3)})
    assert is_sunk(s5) == False

def test_ship_type():
    #add at least one test for ship_type by the deadline of session 7 assignment
    s1 = (0, 0, True, 4, {(0,0), (0,1), (0,2), (0,3)})
    assert ship_type(s1) == "battleship"

    #provide at least five tests in total for ship_type by the project submission deadline    
    s2 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert ship_type(s2) == "cruiser"
    
    s3 = (8, 8, False, 2, {(8,8)})
    assert ship_type(s3) == "destroyer"
    
    s4 = (9, 9, True, 1, set())
    assert ship_type(s4) == "submarine"
    
    s5 = (0, 0, True, 10, {(0,0)})
    assert ship_type(s5) == ""
  
def test_is_open_sea():
    #add at least one test for open_sea by the deadline of session 7 assignment
    fleet1 = []
    assert is_open_sea(2, 3, fleet1) == True
        
    #provide at least five tests in total for open_sea by the project submission deadline
    fleet2 = [(2, 3, True, 4, {(2, 3)})]
    assert is_open_sea(2, 3, fleet2) == False
    assert is_open_sea(8, 8, fleet2) == True
    assert is_open_sea(3, 7, fleet2) == False
    assert is_open_sea(3, 8, fleet2) == True    
 
def test_ok_to_place_ship_at():
    #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    fleet1 = []
    assert ok_to_place_ship_at(2, 3, True, 4, fleet1) == True
        
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline    
    fleet2 = [(2, 3, True, 4, {(2, 3)})]
    assert ok_to_place_ship_at(2, 3, True, 4, fleet2) == False
    assert ok_to_place_ship_at(5, 5, False, 2, fleet2) == True
    fleet2 = [(2, 3, True, 4, {(2, 3)}),(5, 5, False, 2, set())]
    assert ok_to_place_ship_at(8, 8, True, 4, fleet2) == False
    assert ok_to_place_ship_at(8, 8, False, 2, fleet2) == True

def test_place_ship_at():

    #add at least one test for place_ship_at by the deadline of session 7 assignment  
    fleet_v_1 = []
    ship1 = (2, 3, True, 4, set())
    fleet_v_2 = place_ship_at(2, 3, True, 4, fleet_v_1)
    assert fleet_v_2 == [ship1]
    
    # #provide at least five tests in total for place_ship_at by the project submission deadline
    ship2 = (8, 8, False, 2, set())
    fleet_v_3 = place_ship_at(8, 8, False, 2, fleet_v_2)
    assert fleet_v_3 == [ship1, ship2]
    
    ship3 = (5, 5, False, 2, set())
    fleet_v_4 = place_ship_at(5, 5, False, 2, fleet_v_3)
    assert fleet_v_4 == [ship1, ship2, ship3]
    
    ship4 = (8, 0, True, 3, set())
    fleet_v_5 = place_ship_at(8, 0, True, 3, fleet_v_4)
    assert fleet_v_5 == [ship1, ship2, ship3, ship4]

    ship5 = (0, 9, False, 3, set())
    fleet_v_6 = place_ship_at(0, 9, False, 3, fleet_v_5)
    assert fleet_v_6 == [ship1, ship2, ship3, ship4, ship5]

def test_check_if_hits():

    # #add at least one test for check_if_hits by the deadline of session 7 assignment
    fleet1 = [(2, 3, True, 4, set())]
    assert check_if_hits(2, 3, fleet1) == True
    
    # #provide at least five tests in total for check_if_hits by the project submission deadline 
    assert check_if_hits(3, 3, fleet1) == False
    assert check_if_hits(2, 4, fleet1) == True
    assert check_if_hits(2, 7, fleet1) == False
    
    fleet1 = [(2, 3, True, 4, set()), (8, 0, True, 3, set())]
    assert check_if_hits(8, 1, fleet1) == True

def test_hit():
    #add at least one test for hit by the deadline of session 7 assignment

    fleet2 = [(2, 3, True, 4, set())]
    assert hit(2, 3, fleet2) == ([(2, 3, True, 4, {(2, 3)})], (2, 3, True, 4, {(2, 3)}))
        
    #provide at least five tests in total for hit by the project submission deadline
    fleet3 = [(2, 3, True, 4, set()), (8, 0, True, 3, set())]
    assert hit(8, 2, fleet3) == ([(2, 3, True, 4, set()), (8, 0, True, 3, {(8, 2)})], (8, 0, True, 3, {(8, 2)}))
    fleet4 = [(2, 3, True, 4, set()), (8, 0, True, 3, {(8, 2)})]
    assert hit(8, 0, fleet4) == ([(2, 3, True, 4, set()), (8, 0, True, 3, {(8, 2), (8, 0)})], (8, 0, True, 3, {(8, 2), (8, 0)}))
    fleet5 = [(2, 3, True, 4, set()), (8, 0, True, 3, {(8, 2), (8, 0)})]
    assert hit(2, 5, fleet5) == ([(2, 3, True, 4, {(2, 5)}), (8, 0, True, 3, {(8, 2), (8, 0)})], (2, 3, True, 4, {(2, 5)}))
    fleet6 = [(2, 3, True, 4, {(2, 5)}), (8, 0, True, 3, {(8, 2), (8, 0)})]
    assert hit(2, 4, fleet6) == ([(2, 3, True, 4, {(2, 5), (2, 4)}), (8, 0, True, 3, {(8, 2), (8, 0)})], (2, 3, True, 4, {(2, 5), (2, 4)}))

def test_are_unsunk_ships_left():
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    fleet1 = [(2, 3, True, 4, {(2, 3)})]
    assert are_unsunk_ships_left(fleet1) == True
    
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    fleet2 = [(2, 3, True, 4, {(2, 3), (2, 4), (2, 5), (2, 6)})]
    assert are_unsunk_ships_left(fleet2) == False
    
    fleet3 = [(2, 3, True, 4, {(2, 3), (2, 4), (2, 5), (2, 6)}), (8, 0, True, 3, set())]
    assert are_unsunk_ships_left(fleet3) == True
    
    fleet4 = [(3, 1, True, 4, {(3, 2), (3, 1), (3, 3), (3, 4)}), (0, 5, True, 3, set()), (7, 9, False, 3, set()), (9, 3, True, 2, set()), (8, 7, False, 2, set()), (2, 6, False, 2, set()), (6, 7, False, 1, set()), (0, 0, False, 1, set()), (7, 1, False, 1, set()), (4, 8, True, 1, set())]
    assert are_unsunk_ships_left(fleet4) == True
    
    fleet5 = [(3, 1, True, 4, {(3, 2), (3, 1), (3, 3), (3, 4)}), (0, 5, True, 3, {(0, 6), (0, 5), (0, 7)}), (7, 9, False, 3, {(8, 9), (7, 9), (9, 9)}), (9, 3, True, 2, {(9, 3), (9, 4)}), (8, 7, False, 2, {(8, 7), (9, 7)}), (2, 6, False, 2, {(3, 6), (2, 6)}), (6, 7, False, 1, {(6, 7)}), (0, 0, False, 1, {(0, 0)}), (7, 1, False, 1, {(7, 1)}), (4, 8, True, 1, {(4, 8)})]
    assert are_unsunk_ships_left(fleet5) == False


def test_get_open_positions1():
    ocean = Ocean()
    ocean.place_ship_at(2, 0, Battleship(), horizontal=False)
    ocean.place_ship_at(4, 5, Cruiser(), horizontal=False)
    ocean.place_ship_at(5, 8, Cruiser(), horizontal=False)
    ocean.place_ship_at(9, 8, Destroyer(), horizontal=True)
    ocean.place_ship_at(1, 9, Destroyer(), horizontal=False)
    open_positions_1 = ocean.get_open_positions(Destroyer(), horizontal=False)
    assert ((3, 7) in open_positions_1) == False
    open_positions_2 = ocean.get_open_positions(Destroyer(), horizontal=True)
    assert ((3, 7) in open_positions_2) == False

