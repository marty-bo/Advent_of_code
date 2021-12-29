

class Amphipod():
    """This class is not necessary but it cleans the code."""

    def __init__(self, type: str, location: tuple):
        self.type = type
        self.cost = {'A':1,'B':10,'C':100,'D':1000}.get(type, 0)
        self.location = tuple(location)
    
    def get_type(self):
        return self.type
    
    def get_cost(self):
        return self.cost
    
    def get_location(self):
        return self.location
    
    def set_location(self, location):
        self.location = location
    
    def equals(self, amphipod):
        if self.type != amphipod.get_type():
            return False

        if self.cost != amphipod.get_cost():
            return False

        if self.location != amphipod.get_location():
            return False
        
        return True
    
    def clone(self):
        return Amphipod(self.type, tuple(self.location))
