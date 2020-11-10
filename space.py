class Space:  
    is_empty_space = True
    
    def __init__(self):
        is_checked = False
        self.char_representation = "~"
                
    def set_char_representation(self):
        if self.is_checked:
            self.char_representation = "."
        
    def get_char_representation(self):
        return self.char_representation

    def check_shot(self, position):
        self.is_checked = True
        self.set_char_representation()
        
    def is_open_sea(self):
        return True