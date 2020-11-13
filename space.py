class Space:  
    is_empty_space = True

    def __init__(self):
        self.is_checked = False
        self.char_representation = "~"
                
    def set_char_representation(self):
        if self.is_checked and self.is_empty_space:
            self.char_representation = "."
        elif self.is_checked and not self.is_empty_space:
            self.char_representation = "X"
        
    def get_char_representation(self):
        return self.char_representation

    def check_shot(self, position):
        self.is_checked = True
        self.set_char_representation()
        
    def get_type(self):
        return "Space"
        
class Position(Space):
    def __init__(self, row, column, ship):
        super().__init__()
        self.is_empty_space = False
        self.row = row
        self.column = column
        self.ship = ship
        
    def get_position(self):
        return (self.row, self.column)
    
    def set_is_checked(self, is_checked):
        self.is_checked = is_checked
        if self.is_checked:
            super().set_char_representation()
            
    def get_ship_type(self):
        return self.ship.get_ship_type()
        
    def get_type(self):
        return "Position"
        
    def get_ship(self):
        return self.ship
        
    def get_char_representation(self):
        if self.ship.is_sunk():
            return self.ship.get_char_representation()
        else:
            return super().get_char_representation()
        
    