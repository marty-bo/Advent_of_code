import time



def f1(fileName):
    p1_cards = []
    p2_cards = []

    f = open(fileName, 'r')

    f.readline() # 'Player 1:'
    l = f.readline().split()
    while l:
        p1_cards.append(int(l[0]))
        l = f.readline().split()
    
    f.readline() # 'Player 2:'
    l = f.readline().split()
    while l:
        p2_cards.append(int(l[0]))
        l = f.readline().split()
    
    # print(p1_cards)
    # print(p2_cards)

    while p1_cards and p2_cards:
        c1 = p1_cards.pop(0)
        c2 = p2_cards.pop(0)

        if c1 > c2:
            p1_cards.append(c1)
            p1_cards.append(c2)
        else:
            p2_cards.append(c2)
            p2_cards.append(c1)
    
    # print(p1_cards)
    # print(p2_cards)

    w = p1_cards + p2_cards
    # print(w)

    res = 0
    for i in range(len(w)):
        res += w[len(w)-1-i] * (i+1)
    return res

# ####### MAIN #######
f = 'input.txt'

# Part 1-2
start_time = time.time()
res1 = f1(f)
print(res1)
print("--- %s seconds ---" % (time.time() - start_time))
