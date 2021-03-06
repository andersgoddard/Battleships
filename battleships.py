from os import system, name 
from ocean import *
from ships import *
from fleet import *

def clear_console():   
    if name == 'nt': 
        _ = system('cls') #windows   
    else: 
        _ = system('clear') #others

def is_sunk(ship):
    return ship[3] == len(ship[4])

def ship_type(ship):
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
    new_fleet = fleet
    new_ship = (row, column, horizontal, length, set())
    new_fleet.append(new_ship)
    return new_fleet

def randomly_place_all_ships():
    ocean = Ocean()
    fleet = Fleet()
    ocean.build_random_fleet(fleet)   
    game_fleet = []
    
    for ship in fleet.get_fleet():
        game_fleet.append(ship.get_game_representation())
     
    return game_fleet
    
def my_randomly_place_all_ships():
    ocean = Ocean()
    fleet = Fleet()
    ocean.build_random_fleet(fleet)    
    game_fleet = []
    
    for ship in fleet.get_fleet():
        game_fleet.append(ship.get_game_representation())
     
    return (game_fleet, ocean)    

def check_if_hits(row, column, fleet):
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
    sunk_ships = 0
    
    for ship in fleet:
        if ship[3] == len(ship[4]):
            sunk_ships += 1
            
    return sunk_ships != len(fleet)

def main():
    current_fleet, ocean = my_randomly_place_all_ships()
    
    game_over = False
    game_won = False
    shots = 0
    game_feedback = ""
    first_loop = True

    while not game_over: 
        clear_console()
        if first_loop: 
            first_loop = False
            print("BATTLESHIPS by Andrew Goddard\n")
        print(game_feedback)
        ocean.display_ocean()
        loc_str = input("\nEnter row and column separated by a space to shoot (type \"quit\" to end the game early): ")
        if loc_str.lower() == "quit":
            game_over = True
            game_feedback = "\n"
        else:
            try:
                loc_str = loc_str.split()
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
                        game_feedback += "\n"
                else:
                    game_feedback = "You missed!\n\n"
            except:
                game_feedback = "That is an invalid entry!\n\n"

        if not are_unsunk_ships_left(current_fleet): 
            game_over = True
            game_won = True
    
    clear_console()
    final_message = "Game over! "
    if game_won: 
        final_message += "You required "
        final_message += str(shots)
        final_message += " shots.\n\n"
    else:
        final_message += "You gave up!\n\n"
        
    print(final_message)
    ocean.display_ocean()

if __name__ == '__main__': #keep this in
   main()