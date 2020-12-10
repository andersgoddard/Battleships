import pytest
from battleships import *

s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
#we use global variables if certain ships or fleets are used in multiple test functions

def test_is_sunk1():
    assert is_sunk(s) == True
    
def test_ship_type1():
    assert ship_type(s) == "cruiser"


s1 = (2, 3, False, 3, set())
s2 = (6, 9, False, 4, set())
f = [s1, s2]

def test_is_open_sea1(): 
    assert is_open_sea(5,8,f) == False

    
def test_ok_to_place_ship_at1():
    assert ok_to_place_ship_at(5,7, True, 2, f) == False


def test_place_ship_at1():
    actual = place_ship_at(5,6, True, 2, f)
    actual.sort()
    #specification of place_ship_at does not mandate any order on ships in a fleet, so we need
    #to sort expected and actual fleets in order to use == safely 
    expected = [s1, s2, (5,6, True, 2, set())]
    expected.sort()
    assert expected == actual
    

f1 = [(1,1,True, 3, set()), (1,6, False, 2, set()), (2,9, False, 2, set()), (3,0,True, 1, set()), \
              (3,2,True,3, set()), (5,1,True,2, {(5,2)}), (5,4,True,1, set()), (5,7,True,1,set()), (6,9,False,4,set()), (9, 0, True, 1, set()) ] 

    
def test_check_if_hits1():
    assert check_if_hits(5,1,f1) == True
    

def test_hit1():
    (actual,s) = hit(5,1,f1)
    actual.sort()
    expected = [(1,1,True, 3, set()), (1,6, False, 2, set()), (2,9, False, 2, set()), (3,0,True, 1, set()), \
                  (3,2,True,3, set()), (5,1,True,2, {(5,2), (5,1)}), (5,4,True,1, set()), (5,7,True,1,set()), (6,9,False,4,set()), (9, 0, True, 1, set()) ] 
    expected.sort()
    assert (actual, s) == (expected, (5,1,True,2, {(5,2), (5,1)}))

def test_are_unsunk_ships_left1():
    assert are_unsunk_ships_left(f1)==True
