import time


def f1(fileName):
    f = open(fileName, 'r')
    # 0=e, 1=se, 2=sw, 3=w, 4=nw, 5=ne
    # (x, y)
    # [moves if even row, move if odd rows]
    moves = [{'0':(1, 0), '1':(0, 1), '2':(-1, 1), '3':(-1, 0), '4':(-1, -1), '5':(0, -1)},
             {'0':(1, 0), '1':(1, 1), '2':(0, 1), '3':(-1, 0), '4':(0, -1), '5':(1, -1)}]
    # (pos_x, pos_y) : value
    tiles = {}


    for order in f.readlines():
        current_pos = (0, 0)
        order = order.replace('\n', '').replace('se', '1').replace('ne', '5').replace('e','0').replace('sw', '2').replace('nw', '4').replace('w','3')

        for c in order:
            odd = current_pos[1] % 2
            current_pos = (current_pos[0] + moves[odd][c][0], current_pos[1] + moves[odd][c][1])

        if tiles.get(current_pos) is not None:
            tiles[current_pos] = int(tiles[current_pos] == 0)
        else:
            # 0 = white, 1 = black
            tiles[current_pos] = 1

    return tiles, sum([v for v in tiles.values()])




def addWhiteBorder(MAP, map_size):
    '''Add a layer of 0 on each border of the map if there is a 1 in the border
    '''
    top = False
    right = False
    bottom = False
    left = False
    for i in range(len(MAP[0])):
        if MAP[0][i]:
            top = True
        if MAP[-1][i]:
            bottom = True
    for i in range(len(MAP)):
        if MAP[i][0]:
            left = True
        if MAP[i][-1]:
            right = True
    if top:
        MAP.insert(0, [0 for i in range(len(MAP[0]))])
        map_size[1] -= 1
    if bottom:
        MAP.append([0 for i in range(len(MAP[0]))])
        map_size[3] += 1
    if left:
        for i in range(len(MAP)):
            MAP[i].insert(0, 0)
        map_size[0] -= 1
    if right:
        for i in range(len(MAP)):
            MAP[i].append(0)
        map_size[2] += 1

def showHexMap(MAP, odd):
    '''odd = first row is at odd distance from start tile ?
    '''
    for l in MAP:
        if odd:
            print(' ', end='')
            odd = False
        else:
            odd = True
        for c in l:
            print(c, end=' ')
        print('')

def f2(tiles, days):
    # the hex map will be stored in a matrix
    # even rows are not shifted
    # odd rows will be shifted to the left

    #  ... o o ...  =>   o o
    # ... o o o ... => o o o

    # ne, e, se, sw, w, nw
    # (x, y)
    # [dirs in even rows, dirs in odd rows]
    directions = [[(0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1)], 
                  [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 0), (0, -1)]]
    
    # [top_left_x, top_left_y, bottom_right_x, bottom_right_y]
    map_size = [0, 0, 0, 0]
    for coord in tiles:
        if coord[0] < map_size[0]:
            map_size[0] = coord[0]
        elif coord[0] > map_size[2]:
            map_size[2] = coord[0]
        if coord[1] < map_size[1]:
            map_size[1] = coord[1]
        elif coord[1] > map_size[3]:
            map_size[3] = coord[1]
    MAP = []
    for i in range(map_size[3] - map_size[1] + 1):
        MAP.append([])
        for j in range(map_size[2] - map_size[0] + 1):
            MAP[i].append(0)
    for ((x, y), v) in tiles.items():
        MAP[y - map_size[1]][x - map_size[0]] = v
    
    day = 1
    while day <= days:
        # we add a white border to generate black tiles if conditions are respected
        addWhiteBorder(MAP, map_size)
        MAP_copy = [l.copy() for l in MAP]


        # print('')
        # print(map_size)
        # showHexMap(MAP, (map_size[1]) % 2)
        # print('day :', day, 'sum :',sum([sum(MAP[i]) for i in range(len(MAP))]))


        for y in range(len(MAP)):
            odd_row = (map_size[1]+y) % 2
            for x in range(len(MAP[0])):
                nb_neighbors = 0
                for direction in directions[odd_row]:
                    coord = [x + direction[0], y + direction[1]]
                    if coord[0] < 0 or coord[0] >= len(MAP[0]):
                        continue
                    if coord[1] < 0 or coord[1] >= len(MAP):
                        continue
                    nb_neighbors += MAP[coord[1]][coord[0]]
                if MAP[y][x] and (nb_neighbors == 0 or nb_neighbors > 2):
                    MAP_copy[y][x] = 0
                elif not MAP[y][x] and nb_neighbors == 2:
                    MAP_copy[y][x] = 1

        MAP = MAP_copy
        day += 1
    return sum([sum(MAP[i]) for i in range(len(MAP))])

# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
tiles, res1 = f1(f)
print(res1)
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2 - Game of life in a hex grid
start_time = time.time()
res2 = f2(tiles, 100)
print(res2)
print("--- %s seconds ---" % (time.time() - start_time))

