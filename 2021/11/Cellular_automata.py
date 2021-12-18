
class Cellular_automata():

    def __init__(self, energy, neighbors):
        self.hasFlashed = False
        self.energy = energy
        self.neighbors = neighbors
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def increase_energy(self):
        self.energy += 1
    
    def flashes(self):
        if self.energy <= 9 or self.hasFlashed:
            return 0
        self.hasFlashed = True
        flashes_count = 1
        for cell in self.neighbors:
            cell.increase_energy()
        for cell in self.neighbors:
            flashes_count += cell.flashes()
        return flashes_count
    
    def end_step(self):
        if self.hasFlashed:
            self.energy = 0
            self.hasFlashed = False