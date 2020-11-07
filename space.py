class Space:
    is_checked = False
    is_hit = False
    
    def __init__(self):
        self.char_representation = "~"
        
    def set_char_representation(self):
        if self.is_checked and self.is_hit:
            self.char_representation = "X"
        elif self.is_checked and not self.is_hit:
            self.char_representation = "."
        
    def get_char_representation(self):
        return self.char_representation
        
    def get_position(self):
        return self.position
    
    def take_shot(self, successful_hit):
        self.is_checked = True
        if successful_hit:
            self.is_hit = True 
        else:
            self.is_hit = False          
        self.set_char_representation()