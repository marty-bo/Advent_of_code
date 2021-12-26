
import time

def expand_mat(mat:list, value, type):
    width = len(mat[0])
    mat.insert(0, [type(value) for i in range(width)])
    mat.append([type(value) for i in range(width)])

    for i in range(len(mat)):
        mat[i].insert(0, type(value))
        mat[i].append(type(value))


def f(steps):
    
    f = open('input.txt')

    line = f.readline().replace('\n','')
    RULES = {i:1 if line[i]=='#' else 0 for i in range(len(line))}

    border_cell = [0, 0]

    f.readline()
    MAP = []
    for line in f.readlines():
        MAP.append([[1, 1] if c=='#' else [0, 0] for c in line.replace('\n','')])
    f.close()
    expand_mat(MAP, border_cell, list)


    current_index = 0
    next_index = 1
    for step in range(steps):
        height = len(MAP)
        width = len(MAP[0])
        for y in range(height):
            for x in range(width):
                count = 0
                index = 8
                for yy in [-1, 0, 1]:
                    for xx in [-1, 0, 1]:
                        if y+yy < 0 or y+yy >= height or x+xx < 0 or x+xx >= width:
                            count += border_cell[current_index] << index
                        else:
                            count += MAP[y+yy][x+xx][current_index] << index
                        index -= 1
                MAP[y][x][next_index] = RULES.get(count)
        border_cell[next_index] = RULES.get(max(0, (border_cell[current_index] << 9) -1))
        expand_mat(MAP, border_cell, list)
        current_index, next_index = next_index, current_index

    count = 0
    for line in MAP:
        for elm in line:
            count += elm[current_index]

    print('[f]: Steps = %d Lights = %d ' % (steps, count))

    return
    



print("########################################")
start_time = time.time()
f(2)
print("----------- %.8s seconds -----------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f(50)
print("----------- %.8s seconds -----------" % (time.time() - start_time))
