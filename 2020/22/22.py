import time


def readCards(fileName):
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
    
    return p1_cards, p2_cards

def score(deck):
    res = 0
    for i in range(len(deck)):
        res += deck[len(deck)-1-i] * (i+1)
    return res


def f1(fileName):
    p1_cards, p2_cards = readCards(fileName)

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
   
    return score(p1_cards + p2_cards)



def is_superior(c1, c2):
    return c1 > c2

def is_inferior(c1, c2):
    return c1 < c2

def round_in_history(history, current):
    for old in history:
        if len(current[0]) == len(old[0]):
            b = True
            for i in range(len(current[0])):
                if current[0][i] != old[0][i]:
                    b = False
                    break
            if not b:
                continue
            for i in range(len(current[1])):
                if current[1][i] != old[1][i]:
                    break
            if not b:
                continue
            # print(old)
            return 1
    return 0

def recursive_combat(p1_cards, p2_cards, compare, game=0):
    history = []
    # print('Enter a combat.')
    # r = 0
    while p1_cards and p2_cards:
        # print('Game :', game, 'round :', r)
        # r += 1
        if round_in_history(history, [p1_cards, p2_cards]):
            # print(history)
            # print(p1_cards)
            # print(p2_cards)
            # print('in history')
            return 0
        history.append([p1_cards.copy(), p2_cards.copy()])

        c1 = p1_cards.pop(0)
        c2 = p2_cards.pop(0)

        # print(c1, p1_cards)
        # print(c2, p2_cards)
        # print('')

        if len(p1_cards) >= c1 and len(p2_cards) >= c2:
            if recursive_combat(p1_cards[:c1].copy(), p2_cards[:c2].copy(), is_superior, game + 1):
                p2_cards.append(c2)
                p2_cards.append(c1)
            else:   
                p1_cards.append(c1)
                p1_cards.append(c2)
        elif compare(c1, c2):
            p1_cards.append(c1)
            p1_cards.append(c2)
        else:
            p2_cards.append(c2)
            p2_cards.append(c1)
    
    if p1_cards:
        return 0
    else:
         return 1
    


def f2(fileName):
    p1_cards, p2_cards = readCards(fileName)
    if recursive_combat(p1_cards, p2_cards, is_superior):
        return score(p2_cards)
    else:
        return score(p1_cards)





# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
res1 = f1(f)
print(res1)
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
res2 = f2(f)
print(res2)
print("--- %s seconds ---" % (time.time() - start_time))
