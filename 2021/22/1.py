import time
from Cube import Cube



def read_input(filename):
    f = open('input.txt')
    steps = []
    for line in f.readlines():
        line = line.replace('\n', '')
        if line == '':
            continue
        line = line.split(' ')
        type = 1 if line[0] == 'on' else 0
        line = line[1]
        line = line.replace('x=','')
        line = line.replace('y=','')
        line = line.replace('z=','')
        line = line.replace('..',',')
        line = line.split(',')
        line = [int(n) for n in line]
        steps.append((type, line))
    f.close()
    return steps


def f1():

    MIN_X = -50
    MAX_X = 50
    MIN_Y = -50
    MAX_Y = 50
    MIN_Z = -50
    MAX_Z = 50

    steps = read_input('input.txt')

    for i in range(len(steps))[::-1]:
        line = steps[i][1]
        if line[0] < MIN_X or line[1] > MAX_X or line[2] < MIN_Y or line[3] > MAX_Y or line[4] < MIN_Z or line[5] > MAX_Z:
            steps.pop(i)
        pass

    cube = [[[0 for z in range(MIN_Z, MAX_Z+1)] for y in range(MIN_Y, MAX_Y+1)] for x in range(MIN_X, MAX_X+1)]

    for (type, (min_x, max_x, min_y, max_y, min_z, max_z)) in steps:
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                for z in range(min_z, max_z+1):
                    cube[x][y][z] = type

    print('[f1]: Result = %d' % ( sum([sum([sum(a) for a in m]) for m in cube]) ))

    return


def f2():


    steps = read_input('input.txt')
    steps = [(type, Cube(min_x, max_x, min_y, max_y, min_z, max_z)) for (type, (min_x, max_x, min_y, max_y, min_z, max_z)) in steps]
    
    cubes = []
    for (type, cube) in steps:
        tmp_cubes = []
        # switch off all cubes in cube with substraction
        for c in cubes:
            tmp_cubes.extend(c.substract(cube))
        # if the step is to switch on then switch on by adding cube to the list
        if type == 1:
            tmp_cubes.append(cube)
        cubes = tmp_cubes

    count = 0
    for cube in cubes:
        count += cube.get_volume()
    
    print(len(cubes))

    print('[f2]: Result = %d' % (count))

    return



"""
Y          
^   Z      
|  7       
| /        
|/         
o-------->X
"""

print("########################################")
start_time = time.time()
f1()
print("----------- %.8s seconds -----------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f2()
print("----------- %.8s seconds -----------" % (time.time() - start_time))

