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

def is_open_sea(row, column, fleet):
    ocean = Ocean()
    check_position = (row, column)
    closed_positions = set()
    for ship in fleet:
        if ship[3] == 4:
            ship_object = Battleship()
        elif ship[3] == 3:
            ship_object = Cruiser()
        elif ship[3] == 2:
            ship_object = Destroyer()            
        elif ship[3] == 1:
            ship_object = Submarine()
        ship_object.set_starting_row(ship[0])
        ship_object.set_starting_column(ship[1])
        ship_object.set_horizontal_bool(ship[2])
        ship_object.set_hits(ship[4])
        closed_positions.update(ocean.get_closed_positions(ship_object.get_starting_row(), ship_object.get_starting_column(), ship_object, ship_object.get_horizontal_bool()))
    return check_position not in closed_positions

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    pass

def place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    pass

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
