import time



def f1(ips=20, visualisation=False):
    
    f = open('input.txt')
    MAP = []
    for line in f.readlines():
        MAP.append(list(line.replace('\n','')))
    f.close()

    HEIGHT = len(MAP)
    WIDTH = len(MAP[0])

    w = 1.0/float(ips)

    steps = 0
    
    if visualisation:
        print(steps,*[''.join(line) for line in MAP],sep='\n',end='\n\n\n\n')

    changed = True
    while changed:
        t = time.time()
        changed = False
        steps += 1

        # EAST
        target = '>'

        # move sea cucumbers
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if MAP[y][x] == target:
                    if MAP[y][(x+1)%WIDTH] == '.':
                        MAP[y][x] = 'x'
                        MAP[y][(x+1)%WIDTH] = 'o'
                        changed = True

        # translate 'x' and 'o' with '.' and target
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if MAP[y][x] == 'x':
                    MAP[y][x] = '.'
                elif MAP[y][x] == 'o':
                    MAP[y][x] = target

        # SOUTH  
        target = 'v'

        # move other sea cucumbers
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if MAP[y][x] == target:
                    if MAP[(y+1)%HEIGHT][x] == '.':
                        MAP[y][x] = 'x'
                        MAP[(y+1)%HEIGHT][x] = 'o'
                        changed = True
        
        # translate 'x' and 'o' with '.' and target
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if MAP[y][x] == 'x':
                    MAP[y][x] = '.'
                elif MAP[y][x] == 'o':
                    MAP[y][x] = target

        if visualisation:
            while time.time() - t < w:
                pass
            print(*[''.join(line) for line in MAP],sep='\n',end='\n\n\n\n')    

    print('[f1]: Steps = %d' % (steps))

    return



print("########################################")
start_time = time.time()
f1(ips=20, visualisation=True)
print("----------- %.8s seconds -----------" % (time.time() - start_time))

