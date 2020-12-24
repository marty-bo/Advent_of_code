



class Tile():
    def __init__(self, id_ : int, tile : list):
        self.id = id_
        self.tile = tile
        self.top = tile[0]
        self.bottom = tile[-1]
        self.left = ''.join([t[0] for t in tile])
        self.right = ''.join([t[-1] for t in tile])
        # store border as int ('.' = 0; '#' = 1)
        # from LSB to MSB
        # [top, right, bottom, left]
        self.border_val = [0,0,0,0]
        for i in range(len(tile)):
            self.border_val[0] |= (self.top[i] == '#') << i
            self.border_val[1] |= (self.right[i] == '#') << i
            self.border_val[2] |= (self.bottom[i] == '#') << i
            self.border_val[3] |= (self.left[i] == '#') << i
        # [top left, top right, bottom right, bottom left]
        self.corner = [int(self.top[0] == '#'), int(self.top[-1] == '#'), int(self.bottom[-1] == '#'), int(self.bottom[0] == '#')]
    
    def show(self):
        print(self.id)
        print(self.border_val)
        print(self.corner)
        # print only the border of the tile
        print(self.top)
        for i in range(1, len(self.left)-1):
            print(self.left[i], ' '*8, self.right[i], sep='')
        print(self.bottom)
        print('\n')


def readTiles(f):
    tiles = []
    l = f.readline()
    tile = []
    val = 0
    while l:
        if l[0] == 'T':
            val = int(l.split()[1].split(':')[0])
        elif l.split():
            tile.append(l.split()[0])
        else:
            tiles.append(Tile(val, tile))
            val = 0
            tile = []
        l=f.readline()
    tiles.append(Tile(val, tile))
    return tiles

def allPositions(tile : Tile) -> list:
    n = len(tile.tile)
    t_clean = tile.tile
    t_rotation = [''.join([tile.tile[n-1-column][line] for column in range(n)]) for line in range(n)]
    # t_clean = no change
    # t_rotation = 1 rotation right
    # t3 = 2 rotation right
    # t4 = 3 rotation right
    # t5 = no rotation then mirror
    # t6 = 1 rotation right then mirror
    # t7 = 2 rotation right then mirror
    # t8 = 3 rotation right then mirror
    res = [t_clean, t_rotation]
    res.append([''.join([t_clean   [n-1-line][n-1-column] for column in range(n)]) for line in range(n)])
    res.append([''.join([t_rotation[n-1-line][n-1-column] for column in range(n)]) for line in range(n)])
    res.append([''.join([t_clean   [n-1-line][column]     for column in range(n)]) for line in range(n)])
    res.append([''.join([t_rotation[n-1-line][column]     for column in range(n)]) for line in range(n)])
    res.append([''.join([t_clean   [line]    [n-1-column] for column in range(n)]) for line in range(n)])
    res.append([''.join([t_rotation[line]    [n-1-column] for column in range(n)]) for line in range(n)])
    return [Tile(tile.id, t) for t in res]
