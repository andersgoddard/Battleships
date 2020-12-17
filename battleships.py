from os import system, name 
from ocean import *
from ships import *
from fleet import *

#see the readme.md file for description and data 

def clear_console():   
    if name == 'nt': 
        _ = system('cls') #windows   
    else: 
        _ = system('clear') #others

def is_sunk(ship):
    #remove pass and add your implementation
    return ship[3] == len(ship[4])

def ship_type(ship):
    #remove pass and add your implementation
    length = ship[3]
    if length == 4:
        return Battleship().get_type()
    elif length == 3:
        return Cruiser().get_type()
    elif length == 2:
        return Destroyer().get_type()
    elif length == 1:
        return Submarine().get_type()
    else:
        return ""

def create_ship_object(row, column, horizontal, length, hits):
    if length == 4:
        ship_object = Battleship()
    elif length == 3:
        ship_object = Cruiser()
    elif length == 2:
        ship_object = Destroyer()            
    elif length == 1:
        ship_object = Submarine()

    ship_object.set_starting_row(row)
    ship_object.set_starting_column(column)
    ship_object.set_horizontal_bool(horizontal)
    ship_object.set_hits(hits)
    return ship_object

def is_open_sea(row, column, fleet):
    ocean = Ocean()
    check_position = (row, column)
    closed_positions = set()
    for ship in fleet:
        ship_object = create_ship_object(ship[0], ship[1], ship[2], ship[3], ship[4])
        closed_positions.update(ocean.get_closed_positions(ship_object.get_starting_row(), ship_object.get_starting_column(), ship_object, ship_object.get_horizontal_bool()))
    return check_position not in closed_positions

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    ok_to_place = True
    
    for i in range(length):       
        if not ok_to_place:
            break
            
        if (horizontal and row+length > 10) or (not horizontal and column+length > 10):
            ok_to_place = False
        elif horizontal:
            ok_to_place = is_open_sea(row, column+i, fleet)
        else:
            ok_to_place = is_open_sea(row+i, column, fleet)
                
    return ok_to_place
    
def place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    new_fleet = fleet
    new_ship = (row, column, horizontal, length, set())
    new_fleet.append(new_ship)
    return new_fleet

def randomly_place_all_ships():
    #remove pass and add your implementation
    ocean = Ocean()
    fleet = Fleet()
    ocean.build_random_fleet(fleet)   
    game_fleet = []
    
    for ship in fleet.get_fleet():
        game_fleet.append(ship.get_game_representation())
     
    return game_fleet
    
def my_randomly_place_all_ships():
    #remove pass and add your implementation
    ocean = Ocean()
    fleet = Fleet()
    ocean.build_random_fleet(fleet)   # Something in this is causing a bug
    game_fleet = []
    
    for ship in fleet.get_fleet():
        game_fleet.append(ship.get_game_representation())
     
    return (game_fleet, ocean)    

def check_if_hits(row, column, fleet):
    # remove pass and add your implementation
    position = (row, column)
    ocean = Ocean()
    
    hits = False
    
    for ship in fleet:
        if hits:
            break
        ship_object = create_ship_object(ship[0], ship[1], ship[2], ship[3], ship[4])
        ocean.place_ship_at(ship[0], ship[1], ship_object, ship_object.get_horizontal_bool())
        hits = position in ship_object.get_ship_positions()
      
    return hits

def hit(row, column, fleet):
    #remove pass and add your implementation
    position = (row, column)
    ocean = Ocean()

    hit_ship = ()
    return_fleet = []
    
    for ship in fleet:
        ship_object = create_ship_object(ship[0], ship[1], ship[2], ship[3], ship[4])
        ocean.place_ship_at(ship[0], ship[1], ship_object, ship_object.get_horizontal_bool())
        if position in ship_object.get_ship_positions():
            hit_ship = ship
            hit_ship[4].add(position)
            return_fleet.append(ship)
        else:  
            return_fleet.append(ship)
        
    return (return_fleet, hit_ship)
    
def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    sunk_ships = 0
    
    for ship in fleet:
        if ship[3] == len(ship[4]):
            sunk_ships += 1
            
    return sunk_ships != len(fleet)

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet, ocean = my_randomly_place_all_ships()
    
    game_over = False
    game_won = False
    shots = 0
    game_feedback = ""
    print_fleet = False

    # There is a problem with the placement of ships on the board - it is possible to set the starting position of a ship in a place where the remainder of the ship clashes with the closed positions
    while not game_over: 
#        clear_console()
        print(game_feedback)
        if print_fleet:
            print(current_fleet)
            print_fleet = False
        else:
            ocean.display_ocean()
        loc_str = input("Enter row and column separated by a space to shoot (type \"quit\" to end the game early): ")
        if loc_str.lower() == "quit":
            game_over = True
        elif loc_str.lower() == "cheat":
            print_fleet = True
        else:
            loc_str = loc_str.split()    # Need a try except to catch invalid entries here.
            current_row = int(loc_str[0])
            current_column = int(loc_str[1])
            ocean.take_shot(current_row, current_column)
            shots += 1
            if check_if_hits(current_row, current_column, current_fleet):
                game_feedback = "You have a hit!\n"
                (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                if is_sunk(ship_hit):
                    game_feedback += "You sank a " + ship_type(ship_hit) + "!\n"
            else:
                game_feedback = "You missed!\n"

        if not are_unsunk_ships_left(current_fleet): 
            game_over = True
            game_won = True
            
    final_message = "Game over! "
    if game_won: 
        final_message += "You required "
        final_message += str(shots)
        final_message += " shots."

    print(final_message)


if __name__ == '__main__': #keep this in
   main()
