import time

def f1(fileName, moves, debug = False):
    f = open(fileName, 'r')
    cups = [int(n) for n in f.readline().split()[0]]

    current_index = 0
    move = 1
    n = len(cups)
    while move <= moves:
        # current cup value
        current_val = cups[current_index]

        # DEBUG
        if debug:
            print('-- move '+str(move)+' --')
            print('cups: ',end='')
            for i in range(len(cups)):
                if i == current_index:
                    print('(', current_val, ')', sep='', end=' ')
                else:
                    print(cups[i], end=' ')
            print('')

        # three next cups
        three_next = []
        for i in range(1,4):
            three_next.append(cups[(current_index+i)%len(cups)])
        for j in range(3):
            cups.remove(three_next[j])
        
        # DEBUG
        if debug:
            print('pick up: ',end='')
            for i in range(3):
                print(three_next[i], end=' ')
            print('')

        # destination value
        dest_val = current_val
        while dest_val in [current_val] + three_next:
            dest_val -= 1
            dest_val %= n+1
            if dest_val == 0:
                dest_val = n
        
        # DEBUG
        if debug:
            print('destination:', dest_val, end='\n\n')

        # destination index
        dest_ind = -1
        for i in range(len(cups)):
            if cups[i] == dest_val:
                dest_ind = i+1
        for i in range(3)[::-1]:
            cups.insert(dest_ind, three_next.pop(i))

        # shift the list if value at <current_ind> != <current_val>
        while cups[current_index] != current_val:
            cups.insert(0,cups.pop(n-1))

        current_index += 1
        current_index %= n
        move += 1
    

    while cups[0] != 1:
        cups.insert(0,cups.pop(n-1))
    
    return cups

# ####### MAIN #######
f = 'input.txt'
moves = 100

# Part 1
start_time = time.time()
res1 = f1(f, moves)
print(res1)
print("--- %s seconds ---" % (time.time() - start_time))
