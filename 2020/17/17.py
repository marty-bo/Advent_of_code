
import time


# Part 1 - Game of life for an 3d environment

# add layer of 0 on faces of the cube C if there is a 1 in the face
# C[x][y][z]
def expandCube(C : list):
    x_size = len(C)
    y_size = len(C[0])
    z_size = len(C[0][0])
    #print('size :',x_size, y_size, z_size)

    # check wich face need to be expand
    # [x_origin, x_size, y_origin, y_size, z_origin, z_size]
    # 0 : expand useless /// 1 : expand needed
    faces = [0,0,0,0,0,0] 
    # x_origin face
    for i in range(y_size):
        for j in range(z_size):
            if C[0][i][j]:
                faces[0] = 1
                break
        if faces[0]:
            break
    # x_size face
    for i in range(y_size):
        for j in range(z_size):
            if C[x_size-1][i][j]:
                faces[1] = 1
                break
        if faces[1]:
            break
    # y_origin face
    for i in range(x_size):
        for j in range(z_size):
            if C[i][0][j]:
                faces[2] = 1
                break
        if faces[2]:
            break
    # y_size face
    for i in range(x_size):
        for j in range(z_size):
            if C[i][y_size-1][j]:
                faces[3] = 1
                break
        if faces[3]:
            break
    # z_origin face
    for i in range(x_size):
        for j in range(y_size):
            if C[i][j][0]:
                faces[4] = 1
                break
        if faces[4]:
            break
    # z_size face
    for i in range(x_size):
        for j in range(y_size):
            if C[i][j][z_size-1]:
                faces[5] = 1
                break
        if faces[5]:
            break
    
    # add the z layers if needed
    if faces[4]:
        for i in range(x_size):
            for j in range(y_size):
                C[i][j].insert(0, 0)
        z_size += 1
    if faces[5]:
        for i in range(x_size):
            for j in range(y_size):
                C[i][j].insert(z_size, 0)
        z_size += 1
    # add the y layers if needed
    if faces[2]:
        for i in range(x_size):
            C[i].insert(0, [0] * z_size)
        y_size += 1
    if faces[3]:
        for i in range(x_size):
            C[i].insert(y_size, [0] * z_size)
        y_size += 1
    # add the x layers if needed
    if faces[0]:
        l = []
        for i in range(y_size):
            l.append([0] * z_size)
        C.insert(0, l)
        x_size += 1
    if faces[1]:
        l = []
        for i in range(y_size):
            l.append([0] * z_size)
        C.insert(x_size, l)
        x_size += 1


def f1(fileName, cycleLimit):
    f = open(fileName, 'r')
    l = f.readline()
    s = [] # slice input
    while l:
        s.append([1 if c == '#' else 0 for c in l.split()[0]])
        l = f.readline()
    
    C = [s]

    for cycle in range(cycleLimit):
        expandCube(C)
        x_size = len(C)
        y_size = len(C[0])
        z_size = len(C[0][0])
        C_copy = [[C[x][y].copy() for y in range(y_size)] for x in range(x_size)]

        for x in range(x_size):
            for y in range(y_size):
                for z in range(z_size):
                    nb_neighbors = 0
                    for x_bis in range(x-1, x+2):
                        if x_bis >= 0 and x_bis < x_size:
                            for y_bis in range(y-1, y+2):
                                if y_bis >= 0 and y_bis < y_size:
                                    for z_bis in range(z-1, z+2):
                                        if z_bis >= 0 and z_bis < z_size:
                                            if x_bis != x or y_bis != y or z_bis != z:
                                                nb_neighbors += C[x_bis][y_bis][z_bis]
                    if not C[x][y][z] and nb_neighbors == 3:
                        C_copy[x][y][z] = 1
                    elif C[x][y][z] and (nb_neighbors < 2 or nb_neighbors > 3):
                        C_copy[x][y][z] = 0
        C = C_copy
    
    return sum([sum([sum(y) for y in x]) for x in C])




# PART 2 - Generic Function for any dimension (at least >= 2).

# transform a slice (=matrix)(the input) into a <d> dimension array
def sliceToNDimensionCube(s : list, d : int):
    if d < 2:
        print('d invalid.')
        exit(0)
    while d > 2:
        s = [s]
        d -= 1
    return s


# generate an <d> dimension array of size <size>
def generateNDimensionArray(d : int, size : list):
    if d == 0:
        return 0
    else:
        r = []
        for i in range(size[0]):
            r.append(generateNDimensionArray(d-1, size[1:]))
        return  r



# return a tuple (dimension, [sizes]).
def getArrayDimensionAndSize(A : list) -> tuple:
    if not isinstance(A, list):
        return (0, [])
    else:
        r = getArrayDimensionAndSize(A[0])
        r[1].insert(0, len(A))
        return (r[0]+1, r[1])



# for each list L, insert at the start and at the end a list of 0 with the same dimension as other list in L
def expandNDimensionArray(d : int, A : list):
    pass




def f2(fileName, cycleLimit, dimension):
    f = open(fileName, 'r')
    l = f.readline()
    s = [] # slice input
    while l:
        s.append([1 if c == '#' else 0 for c in l.split()[0]])
        l = f.readline()
    C = sliceToNDimensionCube(s, dimension)
    print(C)




# ####### MAIN #######
f = 'bis_input.txt'

# Part 1
# Game of life in 3d space
start_time = time.time()
print(f1(f, 6))
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
# Game of life in 4d space
start_time = time.time()
print(f2(f, 6, 4))
print("--- %s seconds ---" % (time.time() - start_time))

