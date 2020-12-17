
import time
import re








def f1():
    f = open('input.txt', 'r')
    prog = f.readlines()
    f.close()
    for i in range(len(prog)):
        prog[i] = prog[i].split()
        if prog[i][1][0] == '-':
            prog[i][1] = -int(prog[i][1][1:])
        else:
            prog[i][1] = int(prog[i][1][1:])
        prog[i].append(0)

    acc = 0
    num = 0
    while 1:
        if num == len(prog):
            break
        if prog[num][2] != 0:
            break
        else:
            prog[num][2] = num
            
        if prog[num][0] == 'nop':
            num += 1
        elif prog[num][0] == 'acc':
            acc += prog[num][1]
            num += 1
        elif prog[num][0] == 'jmp':
            num += prog[num][1]
    return acc





def f2():
    f = open('input.txt', 'r')
    prog = f.readlines()
    f.close()
    for i in range(len(prog)):
        prog[i] = prog[i].split()
        if prog[i][1][0] == '-':
            prog[i][1] = -int(prog[i][1][1:])
        else:
            prog[i][1] = int(prog[i][1][1:])
        prog[i].append(0)

    acc = 0
    num = 0
    infinite = 1
    while 1:
        if num >= len(prog):
            infinite=0
            break
        if prog[num][2] != 0:
            break
        else:
            prog[num][2] = 1
            
        if prog[num][0] == 'nop':
            prog[num][0]='jmp'
            (a,i) = runBranch([l.copy() for l in prog], num+prog[num][1], acc)
            if i == 0:
                print((a,i))

            prog[num][0]='nop'
            num += 1
        elif prog[num][0] == 'acc':
            acc += prog[num][1]
            num += 1
        elif prog[num][0] == 'jmp':
            prog[num][0]='nop'
            (a,i) = runBranch([l.copy() for l in prog], num+1, acc)
            if i == 0:
                print((a,i))
                
            prog[num][0]='jmp'
            num += prog[num][1]
    return (acc, infinite)



def runBranch(prog, num, acc):
    infinite = 1
    while 1:
        if num >= len(prog):
            infinite = 0
            break
        if prog[num][2] != 0:
            break
        else:
            prog[num][2] = 10
            
        if prog[num][0] == 'nop':
            num += 1
        elif prog[num][0] == 'acc':
            acc += prog[num][1]
            num += 1
        elif prog[num][0] == 'jmp':
            num += prog[num][1]
    return (acc, infinite)

# ####### MAIN #######

# Part 1
start_time = time.time()
print(f1())
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2())
print("--- %s seconds ---" % (time.time() - start_time))

