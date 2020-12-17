
import time



def f1():
    f = open('input.txt', 'r')
    correct = 0
    for line in f.readlines():
        line = line.split()
        v = line[0].split('-')
        vmin = int(v[0])
        vmax = int(v[1])
        c = line[1][0]
        count = 0
        for l in line[2]:
            if c == l:
                count += 1
        if count >= vmin and count <= vmax:
            correct += 1
    print(correct)
    f.close()
    return None


def f2():
    f = open('input.txt', 'r')
    correct = 0
    for line in f.readlines():
        line = line.split()
        v = line[0].split('-')
        vmin = int(v[0])
        vmax = int(v[1])
        c = line[1][0]
        l = line[2]

        if len(l) < vmin:
            pass
        elif l[vmin-1] == c:
            if len(l) < vmax:
                pass
            elif l[vmax-1] != c:
                correct += 1
        elif len(l) >= vmax:
            if l[vmax-1] == c:
                correct += 1

    print(correct)
    f.close()
    return None


start_time = time.time()
f1()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
f2()
print("--- %s seconds ---" % (time.time() - start_time))
