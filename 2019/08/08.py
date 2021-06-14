
import time


def f1(filename, width, height):
    f = [int(c) for c in open(filename).readline().split()[0]]
    layers = int(len(f) / (width*height))
    image = [[[0 for w in range(width)] for h in range(height)] for l in range(layers)]
    l = 0
    h = 0
    w = 0
    digitCount = [[0,0,0] for l in range(layers)]
    for i in range(len(f)):
        image[l][h][w] = f[i]
        if f[i] <= 2:
            digitCount[l][f[i]] += 1
        w += 1
        if w >= width:
            w = 0
            h += 1
            if h >= height:
                h = 0
                l += 1
                if l >= layers:
                    print("FINISH:",l,h,w)
    dmin = digitCount[0]
    for d in digitCount:
        print(d)
        if d[0] < dmin[0]:
            dmin = d
    print(dmin)

    return dmin[1] * dmin[2]
    



def f2(filename, width, height):
    f = [int(c) for c in open(filename).readline().split()[0]]
    layers = int(len(f) / (width*height))
    image = [[[0 for w in range(width)] for h in range(height)] for l in range(layers)]
    l = 0
    h = 0
    w = 0
    res = [[2 for w in range(width)] for h in range(height)]
    for i in range(len(f)):
        image[l][h][w] = f[i]
        if res[h][w] == 2:
            res[h][w] = f[i]
        w += 1
        if w >= width:
            w = 0
            h += 1
            if h >= height:
                h = 0
                l += 1
                if l >= layers:
                    print("FINISH:",l,h,w)
    for l in res:
        for c in l:
            if c == 0:
                print(" ", end="")
            else:
                print("o",end="")
        print("")
    


# Part 1
f = 'input_1.txt'
#f = 'example_1-1.txt'
start_time = time.time()
print(f1(f, 25, 6))
print("--- %s seconds ---" % (time.time() - start_time))


# Part 2
f = 'input_1.txt'
start_time = time.time()
print(f2(f, 25, 6))
print("--- %s seconds ---" % (time.time() - start_time))

