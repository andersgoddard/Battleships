class Space:
    is_hit = False
    
    def __init__(self):
        self.char_representation = "~"
        
    def set_char_representation(self):
        if self.is_hit:
            self.char_representation = "X"
        
    def get_char_representation(self):
        return self.char_representation
        
    def get_position(self):
        return self.position
    
    def take_shot(self):
        self.is_hit = True 
        self.set_char_representation()