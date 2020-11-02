#see the readme.md file for description and data 


def is_sunk(ship):
    #remove pass and add your implementation
    pass

def ship_type(ship):
    #remove pass and add your implementation
    pass

def is_open_sea(row, column, fleet):
    #remove pass and add your implementation
    pass

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
