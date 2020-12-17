
import time
import re








def f1(fileName):
    f = open(fileName, 'r')
    values = sorted([int(l) for l in f.readlines()])
    f.close()
    # print(values)
    stack = [0]
    current = 0
    diff = [0,0,0] # 1, 2, 3
    index = 0

    while(True):
        # print(current, index, diff, stack, sep=' _ ')
        if len(stack) != 0:
            diff[stack[0] - current -1] += 1
            current = stack.pop(0)
        else:
            break

        for i in range(index, min(len(values), index+3)):
            if values[i] - current <= 3 and (len(stack) == 0 or stack[len(stack)-1] < values[i]):
                stack.append(values[i])
        index += 1

        
    return diff, diff[0]*diff[2]




def f2(fileName):
    f = open(fileName, 'r')
    values = sorted([[int(l), 0] for l in f.readlines()])
    f.close()
    

    L = len(values)

    for i in range(min(3, L)):
        if 0 < values[i][0] <=3:
            values[i][1] = 1
    
    for i in range(len(values)):
        for j in range(min(i+1, L), min(i+4, L)):
            if (values[j][0] - values[i][0] <= 3):
                values[j][1] += values[i][1]
    # print(values)
    for v in values[::-1]:
        if v[1] != 0:
            return v
    return 0


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

