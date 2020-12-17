
import time
import re








def f1(fileName):
    f = open(fileName, 'r')
    M = [list(l.split()[0]) for l in f.readlines()]
    f.close()
    
    W = len(M[0])
    H = len(M)

    nbChange = -1
    while nbChange != 0:
        nbChange = 0
        TMP = [l.copy() for l in M]

        for j in range(H):
            for i in range(W):
                tmp = int(0)
                for offX in [-1,0,1]:
                    for offY in [-1,0,1]:
                        if offX == 0 and offY == 0:
                            pass
                        elif i+offX < 0 or i+offX >= W or j+offY < 0 or j+offY >= H:
                            pass
                        elif M[j+offY][i+offX] == '#':
                            tmp += 1

                if M[j][i] == 'L':
                    if tmp == 0:
                        TMP[j][i] = '#'
                        nbChange += 1
                elif M[j][i] == '#':
                    if tmp >= 4:
                        TMP[j][i] = 'L'
                        nbChange += 1
        M = [l.copy() for l in TMP]
    
    occupied = int(0)
    for l in M:
        for s in l:
            if s == '#':
                occupied += 1
    return occupied




def f2(fileName):
    f = open(fileName, 'r')
    M = [list(l.split()[0]) for l in f.readlines()]
    f.close()
    
    W = len(M[0])
    H = len(M)

    nbChange = -1
    while nbChange != 0:
        nbChange = 0
        TMP = [l.copy() for l in M]

        for j in range(H):
            for i in range(W):
                tmp = int(0)
                for offX in [-1,0,1]:
                    for offY in [-1,0,1]:
                        tmpOffX = 0
                        tmpOffY = 0
                        while 1:
                            tmpOffX += offX
                            tmpOffY += offY
                            if tmpOffX == 0 and tmpOffY == 0:
                                break
                            elif i+tmpOffX < 0 or i+tmpOffX >= W or j+tmpOffY < 0 or j+tmpOffY >= H:
                                break
                            elif M[j+tmpOffY][i+tmpOffX] == '#':
                                tmp += 1
                                break
                            elif M[j+tmpOffY][i+tmpOffX] == 'L':
                                break

                if M[j][i] == 'L':
                    if tmp == 0:
                        TMP[j][i] = '#'
                        nbChange += 1
                elif M[j][i] == '#':
                    if tmp >= 5:
                        TMP[j][i] = 'L'
                        nbChange += 1
        M = [l.copy() for l in TMP]
    
    occupied = int(0)
    for l in M:
        for s in l:
            if s == '#':
                occupied += 1
    return occupied







# ####### MAIN #######
f = 'input.txt'

# Part 1
# start_time = time.time()
# print(f1(f))
# print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2(f))
print("--- %s seconds ---" % (time.time() - start_time))

