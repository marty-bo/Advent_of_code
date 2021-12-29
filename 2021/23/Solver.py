
from Configuration import Configuration
from Amphipod import Amphipod
from queue import PriorityQueue


class Solver():
    """The main task of this class is to solve the problem, see https://adventofcode.com/2021/day/23."""

    def __init__(self):
        # map of a configuration
        # . : can move on and can stop on
        # - : can move on but can't stop on
        self.m = [
                '#############',
                list('#..-.-.-.-..#'),
                list('###.#.#.#.###'),
                list('  #.#.#.#.#  '),
                '  #########  ']
    
    def __clear_m(self):
        self.m = [
                '#############',
                list('#..-.-.-.-..#'),
                list('###.#.#.#.###'),
                list('  #.#.#.#.#  '),
                '  #########  ']
    
    def solve(self, initial_configuration: Configuration) -> int:
        """Find the best solution for the configuration <initial_configuration>
        and return the cost of the solution."""

        # configs contains all seen configuration. (hash_code: config)
        configs = dict()

        # PriorityQueue of configurations to analyse (cost, config)
        open_list = PriorityQueue()
        open_list.put((initial_configuration.get_cost(), initial_configuration))

        while not open_list.empty():
            (cost, configuration) = open_list.get() 
            print(cost)

            # if the configuration <configuration> has already been seen
            if configs.get(configuration.get_hash_code(), None) != None:
                continue
            configs[configuration.get_hash_code()] = configuration

            if configuration.is_final():
                return cost
            
            for config in self.__get_possible_next_configurations(configuration):
                open_list.put((config.get_cost(), config))

        return -1

    def __get_possible_next_configurations(self, config) -> list:
        """Return a list of (possible next locations, cost) of an amphipod in the coniguration <config>."""

        next_configs =  list()

        rooms = {'A':3,'B':5,'C':7,'D':9}

        for amphipod in config.get_amphipods():
            # build the map of the configuration <config>
            # . : can move on and can stop on
            # - : can move on but can't stop on
            # #/A/B/C/D : can't move on
            self.__clear_m()

            for _amphipod in config.get_amphipods():
                if _amphipod == amphipod:
                    continue
                (x,y) = _amphipod.get_location()
                self.m[y][x] = _amphipod.get_type()

            # target room of the amphipod
            target_room = rooms.get(amphipod.get_type())

            # if the amphipod is at it's target location then don't move
            (x,y) = amphipod.get_location()
            if x == target_room:
                if y == 3:
                    continue
                if y == 2 and self.m[3][x] == amphipod.get_type():
                    continue

            # locations to analyze
            open_set = set()
            open_set.add((amphipod.get_location(), 0))

            # possible next locations
            close_set = set()

            # if the amphipod is on the hallway
            on_top = amphipod.get_location()[1] == 1

            tmp = '.' + amphipod.get_type()

            # modify the map
            (x,y) = amphipod.get_location()
            # if the amphipod is on the hallway
            if on_top:
                # then it can move on the hallway but can't stop on it
                for i in range(1, 12):
                    if self.m[1][i] == '.':
                        self.m[1][i] = '-'

                # if the target room is 'valid'
                if self.m[2][target_room] in tmp and self.m[3][target_room] in tmp:
                    pass
                # if it is not valid then the amphipod can't move
                else:
                    continue
                
                # the amphipod can't move on rooms that are not the target room
                for i in range(2,4):
                    for j in rooms.values():
                        if j != target_room:
                            self.m[i][j] = '#'
            # elif the amphipod is on a room
            else:
                # it can only move on the target room
                for i in range(2,4):
                    for j in (3,5,7,9):
                        if j != x and j != target_room:
                            self.m[i][j] = '#'
                # if the target room is 'valid'
                if self.m[2][target_room] in tmp and self.m[3][target_room] in tmp:
                    pass
                else:
                    for i in range(2,4):
                        if self.m[i][target_room] == '.':
                            self.m[i][target_room] = '-'
                # it can't stop on it's current current room
                for i in range(2,4):
                    if self.m[i][x] == '.':
                        self.m[i][x] = '-'


            while len(open_set) > 0:
                ((x,y), cost) = open_set.pop()

                # if the amphipod can stop on the locastion
                if self.m[y][x] == '.':
                    close_set.add(((x,y), cost))
                # if the amphipod can only walk on the locastion
                elif self.m[y][x] == '-':
                    pass
                # else if the amphipod can't walk on the location
                else:
                    continue

                # disable the location
                self.m[y][x] = '#'

                # add all contiguous locations to <open_set>
                for (xx,yy) in [(-1,0), (1,0), (0,-1), (0,1)]:
                    if self.m[y+yy][x+xx] in '.-':
                        open_set.add(((x+xx,y+yy), cost + amphipod.get_cost()))
            
            # build all configurations based on <close_set>
            
            other_amphipods = config.get_amphipods()
            other_amphipods.remove(amphipod)

            for (loc, cost) in close_set:
                amphipods = other_amphipods + [Amphipod(amphipod.get_type(), loc)]
                next_configs.append(Configuration(amphipods, config.get_cost() + cost))
        
        return next_configs


