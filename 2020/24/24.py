import time


def f1(fileName, debug = False):
    f = open(fileName, 'r')
    # 0=e, 1=se, 2=sw, 3=w, 4=nw, 5=ne
    # (x, y)
    moves = {'0':(2, 0), '1':(1,1), '2':(-1,1), '3':(-2,0), '4':(-1,-1), '5':(1,-1)}
    # (pos_x, pos_y) : value
    tiles = {}

    for order in f.readlines():
        current_pos = (0, 0)
        order = order.replace('\n', '').replace('se', '1').replace('ne', '5').replace('e','0').replace('sw', '2').replace('nw', '4').replace('w','3')

        for c in order:
            current_pos = (current_pos[0] + moves[c][0], current_pos[1] + moves[c][1])

        if tiles.get(current_pos) is not None:
            tiles[current_pos] = int(tiles[current_pos] == 0)
        else:
            # 0 = white, 1 = black
            tiles[current_pos] = 1

    return sum([v for v in tiles.values()])

# ####### MAIN #######
f = 'bis_input.txt'
debug = True

# Part 1
start_time = time.time()
res1 = f1(f, True)
print(res1)
print("--- %s seconds ---" % (time.time() - start_time))

