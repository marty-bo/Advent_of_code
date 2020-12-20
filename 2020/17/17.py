
import time




# ################################################################
#
# Part 1 - Game of life in a 3d environment
#
# ################################################################

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



# ################################################################
#
# PART 2 - Game of life in a n-dimension environment (at least 2d).
#
# ################################################################

# transform a slice (=matrix)(the input) into a <d> dimension array
def sliceToNDimensionCube(s : list, d : int):
    if d < 2:
        print('d invalid.')
        exit(0)
    while d > 2:
        s = [s]
        d -= 1
    return s


# generate an <d> dimension array of size <size> filled with 0
def generateNDimensionArray(size : list):
    if size == []:
        return 0
    else:
        return [generateNDimensionArray(size[1:]) for i in range(size[0])]


# return a list [sizes].
def getArraySize(A : list) -> list:
    if not isinstance(A, list):
        return []
    else:
        r = getArraySize(A[0])
        r.insert(0, len(A))
        return r

# print(getArraySize([[[1,2,3]]]))


# for each list L, insert at the start and at the end a list of 0 with the same dimension as other list in L
# TODO : add the list only if there is a 1 in the face
def expandNDimensionArray(A : list):
    if not isinstance(A, list):
        return
    for l in A:
        expandNDimensionArray(l)
    v = getArraySize(A[0])
    A.insert(0, generateNDimensionArray(v))
    A.append(generateNDimensionArray(v))

# a = [[1,1]]
# expandNDimensionArray(a)
# print(a)




# copy a n-dimension array
def copyNDimensionArray(A : list):
    if not isinstance(A, list):
        return A
    else:
        return [copyNDimensionArray(a) for a in A]



def getNeighborsCount(A : list, pos : list) -> int:
    if not isinstance(A, list):
        return int(A != 0)
    else:
        n = 0
        if pos[0] > 0:
            n += getNeighborsCount(A[pos[0]-1], pos[1:])
        if pos[0] < len(A)-1:
            n += getNeighborsCount(A[pos[0]+1], pos[1:])
        n += getNeighborsCount(A[pos[0]], pos[1:])
        return n

# return the value of a case at pos <pos>
def getValueAtPos(A : list, pos : list):
    if not isinstance(A, list):
        return int(A != 0)
    else:
        return getValueAtPos(A[pos[0]], pos[1:])


# set value at pos <pos> in a n-dimension array <A>
def setValueAtPos(A : list, pos : list, val : int):
    if not isinstance(A[pos[0]], list):
        A[pos[0]] = val
    else:
        setValueAtPos(A[pos[0]], pos[1:], val)



def cycleCore(A : list, cycleLimit : int):

    # for each cycle
    while cycleLimit:
        expandNDimensionArray(A)
        A_copy = copyNDimensionArray(A)
        
        # get the size of the n-dimension array A
        size = getArraySize(A_copy)
        n = len(size)
        # generate a list of n values representing the pos in the n-dimension array
        pos = [0] * n

        # for each case
        while pos[0] != size[0]:
            nb_neighbors = getNeighborsCount(A, pos)
            alive = getValueAtPos(A, pos)
            nb_neighbors -= alive
            if alive:
                if nb_neighbors < 2 or nb_neighbors > 3:
                    setValueAtPos(A_copy, pos, 0)
            else:
                if nb_neighbors == 3:
                    setValueAtPos(A_copy, pos, 1)

            # increment the position
            pos[-1] += 1
            for i in range(n-1, 0, -1):
                if pos[i] == size[i]:
                    if i != 0:
                        pos[i-1] += 1
                        pos[i] = 0
        # next cycle
        cycleLimit -= 1
        # copy the new array
        A = A_copy
    return A
    
# count number of values != 0 in an n-dimension array
def countAliveCube(A : list):
    if not isinstance(A, list):
        return A != 0
    else:
        return sum([countAliveCube(a) for a in A])


def f2(fileName, cycleLimit, dimension):
    f = open(fileName, 'r')
    l = f.readline()
    s = [] # slice input
    while l:
        s.append([1 if c == '#' else 0 for c in l.split()[0]])
        l = f.readline()
    C = sliceToNDimensionCube(s, dimension)
    C = cycleCore(C, cycleLimit)
    return countAliveCube(C)




# ####### MAIN #######
f = 'input.txt'

# Part 1
# Game of life in 3d space
start_time = time.time()
print(f1(f, 6))
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2 - not well optimised
# Game of life in n-dimension space
start_time = time.time()
# 6 cycle in a 4d space
print(f2(f, 6, 4))
print("--- %s seconds ---" % (time.time() - start_time))

