
import time


def f1(fileName):
    pos = [0,0] # +N -S / +E -W
    rot = 1 # current rotation N, E, S, W / 0, 1, 2, 3

    f = open(fileName, 'r')
    actions = [l.split()[0] for l in f.readlines()]
    f.close()

    for a in actions:
        if a[0] == 'N':
            pos[0] += int(a[1:])
        elif a[0] == 'S':
            pos[0] -= int(a[1:])
        elif a[0] == 'E':
            pos[1] += int(a[1:])
        elif a[0] == 'W':
            pos[1] -= int(a[1:])

        elif a[0] == 'F':
            pos[0] += int(a[1:])*(1 if rot==0 else -1 if rot==2 else 0)
            pos[1] += int(a[1:])*(1 if rot==1 else -1 if rot==3 else 0)

        elif a[0] == 'R':
            rot = (rot + int(a[1:])/90) % 4
        elif a[0] == 'L':
            rot = (4 + rot - int(a[1:])/90) % 4


    return pos, abs(pos[0])+abs(pos[1])



def f2(fileName):
    pos = [0,0] # +N -S / +E -W
    waypoint = [1,10] # +N -S / +E -W

    f = open(fileName, 'r')
    actions = [l.split()[0] for l in f.readlines()]
    f.close()

    for a in actions:
        if a[0] == 'N':
            waypoint[0] += int(a[1:])
        elif a[0] == 'S':
            waypoint[0] -= int(a[1:])
        elif a[0] == 'E':
            waypoint[1] += int(a[1:])
        elif a[0] == 'W':
            waypoint[1] -= int(a[1:])
        elif a[0] == 'F':
            pos[0] += int(a[1:])*waypoint[0]
            pos[1] += int(a[1:])*waypoint[1]

        elif a[0] == 'R':
            for i in range(int(int(a[1:])/90)):
                waypoint[0], waypoint[1] = -1*waypoint[1], waypoint[0]
        elif a[0] == 'L':
            for i in range(int(int(a[1:])/90)):
                waypoint[0], waypoint[1] = waypoint[1], -1*waypoint[0]


    return pos, abs(pos[0])+abs(pos[1])


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

