
import time
import re








def f1(fileName, r):
    f = open(fileName, 'r')
    values = [int(l) for l in f.readlines()]
    f.close()
    for i in range(r, len(values)):
        v = values[i]
        exist = False
        for j in range(i-r, i):
            vtmp = v - values[j]
            if vtmp in values[i-r:i] and vtmp != values[j]:
                exist = True
                #print(v, values[j], vtmp)
                break
        if not exist:
            print(v)
    return 1





def f2(fileName, target):
    f = open(fileName, 'r')
    values = [int(l) for l in f.readlines()]
    f.close()
    s = 0
    j = -1
    for i in range(len(values)):
        while s < target:
            j += 1
            s += values[j]
        if s == target:
            return min(values[i:j+1]) +  max(values[i:j+1])
        else:
            s -= values[i]

        
    return 1


# ####### MAIN #######

# Part 1
start_time = time.time()
print(f1('input.txt', 25))
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2('input.txt', 1309761972))
print("--- %s seconds ---" % (time.time() - start_time))
