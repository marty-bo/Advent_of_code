
import time

def f1():
    horizontal = 0
    depth = 0
    f = open('input.txt', 'r')
    for l in [l.split() for l in f.readlines()]:
        if l[0] == 'forward':
            horizontal += int(l[1])
        elif l[0] == 'up':
            depth -= int(l[1])
        else:
            depth += int(l[1])
    print('[f1]:', '\nhorizontal:',horizontal, '\ndepth:',depth, '\nhorizontal * depth:', horizontal * depth)
    return


def f2():
    horizontal = 0
    depth = 0
    aim = 0
    f = open('input.txt', 'r')
    for l in [l.split() for l in f.readlines()]:
        if l[0] == 'forward':
            horizontal += int(l[1])
            depth += aim * int(l[1])
        elif l[0] == 'up':
            aim -= int(l[1])
        else:
            aim += int(l[1])
    print('[f2]:', '\nhorizontal:',horizontal, '\ndepth:',depth, '\naim:',aim, '\nhorizontal * depth:', horizontal * depth)
    return


print("------------------")
start_time = time.time()
f1()
print("--- %s seconds ---" % (time.time() - start_time))


print("------------------")
start_time = time.time()
f2()
print("--- %s seconds ---" % (time.time() - start_time))
