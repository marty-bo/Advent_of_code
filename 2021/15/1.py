
import time
from A_star import A_star, matrix_to_list

def f(repetitions=0):

    f = open('input.txt')

    MAP = []

    # read map
    for line in f.readlines():
        MAP.append([int(n) for n in line.replace('\n', '')])
    f.close()

    HEIGHT = len(MAP)
    WIDTH = len(MAP[0])

    # repeat the map
    for rep in range(1, repetitions):
        for i in range(HEIGHT):
            MAP[i].extend([max(1, (MAP[i][(rep-1)*WIDTH+j] + 1) % 10) for j in range(WIDTH)])
    WIDTH = len(MAP[0])

    # repeat the map on the bottom
    for rep in range(1, repetitions):
        for i in range(HEIGHT):
            MAP.append([max(1, (MAP[(rep-1)*HEIGHT+i][j] + 1) % 10) for j in range(WIDTH)])
    HEIGHT = len(MAP)

    # print(*MAP, sep='\n')

    MAP_list = matrix_to_list(MAP, WIDTH, HEIGHT)
    # print(MAP_list)
    astar = A_star(MAP_list)
    path = astar.search(0, len(MAP_list)-1)
    cost = 0
    for index in path[1:]:
        cost += MAP_list[index][0]
    cost -= MAP_list[0][0]

    print('[f]: Repetitions = %d Lowest risk = %d' % (repetitions, cost))

    return 0
    



print("########################################")
start_time = time.time()
f()
print("----------- %.8s seconds -----------" % (time.time() - start_time))

print("########################################")
start_time = time.time()
f(5)
print("----------- %.8s seconds -----------" % (time.time() - start_time))
