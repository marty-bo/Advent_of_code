
import time


def f1(fileName):
    f = open(fileName, 'r')
    h = int(f.readline())
    B = []
    for b in f.readline().split(','):
        if b != 'x':
            B.append(int(b))
    f.close()
    tmin = (B[0]-h % B[0], B[0])
    for b in B:
        if b-h % b < tmin[0]:
            tmin = (b-h % b, b)
    return tmin, tmin[0]*tmin[1]




def f2(fileName):
    f = open(fileName, 'r')
    h = int(f.readline())
    B = []
    i = 0
    for b in f.readline().split(','):
        if b != 'x':
            B.append([int(b), -i])
        i += 1
    f.close()

    N = 1
    for b in B:
        N *= b[0]
    print(N)
    Ni = []
    for b in B:
        Ni.append(int(N/b[0]))
    
    Xi = []
    print(list(zip(B,Ni)))
    for (b, n) in list(zip(B,Ni)):
        v = n%b[0]
        if v == 1:
            Xi.append(v)
        else:
            for j in range(1,b[0]):
                if (v*j) % b[0] == 1:
                    Xi.append(j)
                    break
    print(Xi)

    BiNiXi = []
    for (b,n,x) in list(zip(B,Ni,Xi)):
        BiNiXi.append(b[1]*n*x)
    print(BiNiXi)
    return sum(BiNiXi) % N

    # timestamp = 0
    # n = len(B)
    # while 1:
    #     # print(timestamp)
    #     i = 0
    #     for t in B:
    #         tmp = 0
    #         total = 0
    #         if (timestamp + t[1]) % t[0]:
    #             # print(timestamp, t, (timestamp + t[1]) % t[0])
    #             if total == 0:
    #                 total = t[0] - (timestamp + t[1]) % t[0]
    #             else:
    #                 tmp = t[0] - (timestamp + t[1]) % t[0]
    #                 if (timestamp + total) % tmp != 0:
    #                     total *= tmp
    #         else:
    #             i += 1
    #         timestamp += total
    #     if i == n:
    #         return timestamp





# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2(f))
print("--- %s seconds ---" % (time.time() - start_time))

