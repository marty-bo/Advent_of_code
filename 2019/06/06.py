
import time


class Node:
    def __init__(self, val):
        self.value = val
        self.satellites = dict()



def orbitCount(node, d):
    r = d
    d += 1
    for v in node.satellites.values():
        r += orbitCount(v, d)
    return r


def f1(fileName):
    file = open(fileName)
    s = file.readline().replace('\n', '').split(')')
    # build the tree
    objects = dict()
    p = Node(s[0])
    c = Node(s[1])
    p.satellites[s[1]] = c
    objects[s[0]] = p
    objects[s[1]] = c
    while s != ['']:
        p = objects.get(s[0])
        if p == None:
            p = Node(s[0])
            objects[s[0]] = p
        c = objects.get(s[1])
        if c == None:
            c = Node(s[1])
            objects[s[1]] = c
        p.satellites[s[1]] = c
        s = file.readline().replace('\n', '').split(')')

    # print the tree
    if False:
        for k in objects.keys():
            print(objects[k].value)
            for k2 in objects[k].satellites.keys():
                print(" \___",objects[k2].value)
    
    # calcul the total number of direct and indirect orbits
    for v in objects.values():
        if v.value == 'COM':
            return orbitCount(v, 0)
    return 0




# Part 1
f = 'input_1.txt'
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

