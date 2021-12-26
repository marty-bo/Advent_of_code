import time




def f1():
    
    f = open('input.txt')
    pos_p1 = int(f.readline().replace('\n', '').replace('Player 1 starting position: ', ''))
    pos_p2 = int(f.readline().replace('\n', '').replace('Player 2 starting position: ', ''))
    f.close()

    dice = 1

    pos = [pos_p1, pos_p2]
    scores = [0, 0]

    turn = 0
    dice_rolled_count = 0

    while scores[0] < 1000 and scores[1] < 1000:
        rolls = 0
        for i in range(3):
            dice_rolled_count += 1
            rolls += dice 
            dice = dice + 1
            if dice > 100:
                dice = 1
        pos[turn] = (pos[turn] - 1 + rolls) % 10 + 1
        scores[turn] += pos[turn]
        turn = 0 if turn == 1 else 1
    print(scores)
    print('[f1]: Result = %d' % (min(scores) * dice_rolled_count))

    return



ROLL_FREQUENCY = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

def get_next_pos(pos, score):
    return (pos - 1 + score) % 10 + 1


def wins(pos_p1, score_p1, pos_p2, score_p2):
    win_p1 = 0
    win_p2 = 0

    for (score, occur) in ROLL_FREQUENCY:
        tmp_pos_p1 = get_next_pos(pos_p1, score)
        if score_p1+tmp_pos_p1 >= 21:
            win_p1 += occur
            continue
        w_p2, w_p1 = wins(pos_p2, score_p2, tmp_pos_p1, score_p1+tmp_pos_p1)
        win_p1 += w_p1 * occur
        win_p2 += w_p2 * occur
    
    return win_p1, win_p2

def f2():
    
    f = open('input.txt')
    pos_p1 = int(f.readline().replace('\n', '').replace('Player 1 starting position: ', ''))
    pos_p2 = int(f.readline().replace('\n', '').replace('Player 2 starting position: ', ''))
    f.close()

    (win_p1, win_p2) = wins(pos_p1, 0, pos_p2, 0)
    print(win_p1, win_p2)

    print('[f2]: Result = %d' % (0))

    return
    


print("########################################")
start_time = time.time()
f1()
print("----------- %.8s seconds -----------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f2()
print("----------- %.8s seconds -----------" % (time.time() - start_time))

