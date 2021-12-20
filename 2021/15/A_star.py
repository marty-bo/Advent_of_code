from os import close
from queue import PriorityQueue


def matrix_to_list(mat, width, height):
    """
    Transform a matrix to a list for A_star class
    """
    mat_list = []
    for y in range(height):
        for x in range(width):
            cost = mat[y][x]
            neighbors = []
            if y > 0:
                neighbors.append((y-1)*width + x)
            if y < height-1:
                neighbors.append((y+1)*width + x)
            if x > 0:
                neighbors.append(y*width + (x-1))
            if x < height-1:
                neighbors.append(y*width + (x+1))
            mat_list.append((cost, neighbors))
    return mat_list

class A_star():

    def __init__(self, MAP):
        """
        MAP is a list of tuple (cost, neighbors_coords)
        with cost an int and neighbors_coords an iterable of the indexes of neighbors MAP
        """
        self.MAP = MAP
    
    def search(self, start_node_coord, end_node_coord):
        open_list = PriorityQueue()
        # PriorityQueue of (node, parent_node)
        open_list.put((self.MAP[start_node_coord][0], (start_node_coord, None)))
        # node_coord : parent_node_coord 
        close_list = dict()
        while not open_list.empty():
            path_cost, (current_node_coord, parent_node_coord) = open_list.get()
            # if a path already exist for the current node
            if close_list.get(current_node_coord, -1) != -1:
                # forget the current path
                continue
            # (if no path) add the current path
            close_list[current_node_coord] = parent_node_coord
            # if the path reached the end
            if current_node_coord == end_node_coord:
                path = []
                while current_node_coord != -1:
                    path.append(current_node_coord)
                    current_node_coord = close_list.get(current_node_coord, -1)
                return path[::-1]
            # read informations about the current node
            (cost, neighbors) = self.MAP[current_node_coord]
            # build all possible paths
            for neighbor in neighbors:
                open_list.put((path_cost + cost, (neighbor, current_node_coord)))
        print(open_list)
        return []