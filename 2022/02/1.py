
import time
import os

input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

def calcul_score(rules: dict, rounds: list[tuple[str, str]]) -> int:
    score = 0
    for pA, pB in rounds:
        score += rules[(pA, pB)]
    return score

def which_shape(opponent_shape:str, round_result: str):
    """
    Return the needed shape for a given context.
    opponent_shape: A=Rock, B=Paper, C=Scissors
    round_result: X=lose, Y=draw, Z=win.
    Return: X=Rock, Y=Paper, Z=Scissors
    """
    if opponent_shape == 'A':
        if round_result == 'X':
            return 'Z'
        elif round_result == 'Y':
            return 'X'
        return 'Y'
    elif opponent_shape == 'B':
        if round_result == 'X':
            return 'X'
        elif round_result == 'Y':
            return 'Y'
        return 'Z'
    if round_result == 'X':
        return 'Y'
    elif round_result == 'Y':
        return 'Z'
    return 'X'

def f1():
    f = open(input_file_path)
    lines = f.readlines()
    f.close()
    battle_result = {
        ('A','X'):3 + 1,
        ('A','Y'):6 + 2,
        ('A','Z'):0 + 3,
        ('B','X'):0 + 1,
        ('B','Y'):3 + 2,
        ('B','Z'):6 + 3,
        ('C','X'):6 + 1,
        ('C','Y'):0 + 2,
        ('C','Z'):3 + 3,
    }
    rounds = map(lambda l: tuple(l.replace('\n', '').split(' ')), lines)
    score = calcul_score(battle_result, rounds)
    print("Your score is %d" % score)
    return

def f2():
    f = open(input_file_path)
    lines = f.readlines()
    f.close()
    rounds = [tuple(l.replace('\n', '').split(' ')) for l in lines]
    battle_result = {
        ('A','X'):3 + 1,
        ('A','Y'):6 + 2,
        ('A','Z'):0 + 3,
        ('B','X'):0 + 1,
        ('B','Y'):3 + 2,
        ('B','Z'):6 + 3,
        ('C','X'):6 + 1,
        ('C','Y'):0 + 2,
        ('C','Z'):3 + 3,
    }
    score = calcul_score(battle_result, map(lambda r: (r[0], which_shape(r[0], r[1])), rounds))
    print("Your score is %d" % score)
    return


print("Begin task 1...")
start_time = time.time()
f1()
print("End task 1 in  %.8s seconds." % (time.time() - start_time))


print("Begin task 2...")
start_time = time.time()
f2()
print("End task 2 in  %.8s seconds." % (time.time() - start_time))
