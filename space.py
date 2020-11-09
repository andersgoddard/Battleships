class Space:  
    is_empty_space = True
    
    def __init__(self):
        is_checked = False
        self.char_representation = "~"
        
                
    def set_char_representation(self):
        if self.is_checked and self.is_hit:
            self.char_representation = "X"
        elif self.is_checked and not self.is_hit:
            self.char_representation = "."
        
    def get_char_representation(self):
        return self.char_representation

    def check_shot(self, position):
        if self.is_empty_space:
            self.is_hit = False 
        else:
            self.is_hit = True          
        
        self.is_checked = True
        self.set_char_representation()
        
    def is_open_sea(self):
        return True