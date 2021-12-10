
import time
import bingo_board as board


def f1():
    f = open('input.txt', 'r')
    
    numbers = [int(n) for n in f.readline().replace('\n','').split(',')]
    f.readline()

    # list of all boards on the game
    boards = []

    tmp = []
    for line in f:
        line = [int(n) for n in line.split()]
        if len(line) == 0:
            boards.append(board.Board(tmp))
            tmp = []
        else:
            tmp.append(line)
        
    f.close()

    winScore = 0
    for n in numbers:
        for b in boards:
            b.tick(n)
            if b.hasWin():
                winScore = n * b.getSumOfUnticked()
                break
        if winScore != 0:
            break

    print('[f1]: winScore = {}\n'.format(winScore))
    return



def f2():
    f = open('input.txt', 'r')
    
    numbers = [int(n) for n in f.readline().replace('\n','').split(',')]
    f.readline()

    # list of all boards on the game
    boards = []

    tmp = []
    for line in f:
        line = [int(n) for n in line.split()]
        if len(line) == 0:
            boards.append(board.Board(tmp))
            tmp = []
        else:
            tmp.append(line)
        
    f.close()

    winScore = 0
    for n in numbers:
        for b in boards[::-1]:
            b.tick(n)
            if b.hasWin():
                boards.remove(b)
                if len(boards) == 0:
                    winScore = n * b.getSumOfUnticked()
        if winScore != 0:
            break

    print('[f2]: winScore = {}\n'.format(winScore))
    return


print("------------------")
start_time = time.time()
f1()
print("--- %s seconds ---" % (time.time() - start_time))

print("------------------")
start_time = time.time()
f2()
print("--- %s seconds ---" % (time.time() - start_time))

