class Space:
    def __init__(self):
        self.char_representation = ""
        
    def get_char_representation(self):
        return self.char_representation

class EmptySpace(Space):
    def __init__(self):
        self.char_representation = "~"
    
class OccupiedSpace(Space):
    def __init__(self):
        self.char_representation = "X"