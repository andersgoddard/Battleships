from ocean import *
from ships import *
from fleet import *

#see the readme.md file for description and data 


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
            ok_to_place = is_open_sea(row+i, column, fleet)
        else:
            ok_to_place = is_open_sea(row, column+i, fleet)
                
    return ok_to_place
    
def place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    new_fleet = fleet
    new_ship = (row, column, horizontal, length, {})
    new_fleet.append(new_ship)
    return new_fleet

def randomly_place_all_ships():
    #remove pass and add your implementation
    pass  

def check_if_hits(row, column, fleet):
    #remove pass and add your implementation
    pass

def hit(row, column, fleet):
    #remove pass and add your implementation
    pass

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    pass

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_shis_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
