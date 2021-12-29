

from Amphipod import Amphipod


class Configuration():
    """The class Configuration contains all relevant informations of a configuration."""

    def __init__(self, amphipods: list, cost: int):
        self.amphipods = amphipods
        self.cost = cost

        # Hash code is a string containing all the amphipods location ordered 
        # by they type and location.
        # This hash code is not unique for example if we switch two amphipod 
        # of the same type the hash code is still the same.
        # But this is not a problem because amphipod are not identified.
        hash_code = ''
        tmp = {'A':[],'B':[],'C':[],'D':[]}
        for amphipod in amphipods:
            tmp[amphipod.get_type()].append(amphipod.get_location())
        for k in 'ABCD':
            for (x,y) in sorted(tmp[k]):
                hash_code += str(x) + str(y)
        
        self.hash_code = hash_code

    def is_final(self):
        """Return True if the configuration is final."""
        for amphipod in self.amphipods:
            if amphipod.get_type() == 'A':
                if amphipod.get_location() not in [(3,2), (3,3)]:
                    return False
            elif amphipod.get_type() == 'B':
                if amphipod.get_location() not in [(5,2), (5,3)]:
                    return False
            elif amphipod.get_type() == 'C':
                if amphipod.get_location() not in [(7,2), (7,3)]:
                    return False
            elif amphipod.get_type() == 'D':
                if amphipod.get_location() not in [(9,2), (9,3)]:
                    return False
        return True
    
    def get_amphipods(self):
        return list(self.amphipods)
    
    def get_cost(self):
        return self.cost

    def get_hash_code(self) -> int:
        """Return a code (probably not unique) to identify the configuration."""
        return self.hash_code
    
    def equals(self, config) -> bool:
        """Return True is the current configuration is the same as <config>."""
        if self.hash_code != config.get_hash_code():
            return False
        
        found = False
        for amphipod in self.amphipods:
            found = False
            for a in config.get_amphipods:
                if amphipod.equals(a):
                    found = True
                    break
            if found == False:
                break
        return True
    
    def __lt__(self, other) -> bool:
        """Override the '<' operator for the PriorityQueue."""
        return True
    
    def to_string(self) -> str:
        """Return the string version of the current configuration."""
        res = [
                 '#############' ,
            list('#...........#'),
            list('###.#.#.#.###'),
            list('  #.#.#.#.#  '),
                 '  #########  ']
        
        for amphipod in self.amphipods:
            (x,y) = amphipod.get_location()
            res[y][x] = amphipod.get_type()

        for i in range(1, 4):
            res[i] = ''.join(res[i])
        
        res = '\n'.join(res)
        
        return res
    
    def clone(self):
        return Configuration(self.previous_configuration, list(self.amphipods), self.cost)


def string_to_config(map: list, cost: int) -> Configuration:
    """Return a configuration defined by <map> a list of string."""
    amphipods = list()
    for i in range(1, 12):
        if map[1][i] not in '.#':
            amphipods.append(Amphipod(map[1][i], (i,1)))
    for i in range(2,4):
        for j in (3,5,7,9):
            if map[i][j] not in '.#':
                amphipods.append(Amphipod(map[i][j], (j,i)))
    
    return Configuration( amphipods, cost)




if __name__ == '__main__':
    amphipods = list()
    amphipods.append(Amphipod('A', (3,2)))
    amphipods.append(Amphipod('A', (3,3)))
    amphipods.append(Amphipod('B', (5,2)))
    amphipods.append(Amphipod('B', (5,3)))
    amphipods.append(Amphipod('C', (7,2)))
    amphipods.append(Amphipod('C', (7,3)))
    amphipods.append(Amphipod('D', (9,2)))
    amphipods.append(Amphipod('D', (9,3)))
    config = Configuration(amphipods, 0)
    print(config.to_string())
    print(config.is_final())