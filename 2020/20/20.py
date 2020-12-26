import time
from math import sqrt
from tile import *


UP = (0, 1)
LEFT = (-1, 0)
DOWN = (0, -1)
RIGHT = (1, 0)
DIRS = [UP, DOWN, LEFT, RIGHT]


def compatible(tile1, tile2, dir):
    """
    tile1 is at (x,y)
    tile2 is at (x+dir[0], y+dir[1])
    """
    i1 = 0
    i2 = 0
    if dir == DOWN:
        i1 = 0
        i2 = 2
    elif dir == RIGHT:
        i1 == 3
        i2 == 1
    elif dir == UP:
        i1 = 2
        i2 = 0
    else:
        i1 = 1
        i2 = 3
    return tile1.border_val[i1] == tile2.border_val[i2]




def f1(fileName : str):
    f = open(fileName, 'r')
    tiles = readTiles(f)
    allPossibleTiles = []
    for tile in tiles:
        #tile.show()
        allPossibleTiles += allPositions(tile)
    size = int(sqrt(len(tiles)))
    puzzle = [[None for i in range(size)] for j in range(size)]
    checkNeighbors(allPossibleTiles)

    used = {t.id : 0 for t in tiles}
    for i in range(size):
        for j in range(size):
            # [top, right, bottom, left]
            needNeighbors = [int(i!=0), int(j<size-1), int(i<size-1), int(j!=0)]
            for tile in allPossibleTiles:
                if not used[tile.id]:
                    if needNeighbors[0] != int(len(tile.neighbors[0])!=0):
                        continue
                    if needNeighbors[1] != int(len(tile.neighbors[1])!=0):
                        continue
                    if needNeighbors[2] != int(len(tile.neighbors[2])!=0):
                        continue
                    if needNeighbors[3] != int(len(tile.neighbors[3])!=0):
                        continue
                    
                    if needNeighbors[0] and tile.border_val[0] != puzzle[i-1][j].border_val[2]:
                        continue
                    if needNeighbors[3] and tile.border_val[3] != puzzle[i][j-1].border_val[1]:
                        continue
                    puzzle[i][j] = tile
                    used[tile.id] = 1
                    break
    for l in puzzle:
        for c in l:
            print(c.id, end=' ')
        print('')
    return puzzle[0][0].id * puzzle[0][size-1].id * puzzle[size-1][0].id * puzzle[size-1][size-1].id
    

# ####### MAIN #######
f = 'input.txt'
# Part 1
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

