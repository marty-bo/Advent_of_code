
import time



class EarleyAlgorithm:
    def __init__(self, word : list, rules : dict, source : str):
        self.items = []
        self.word = word
        self.rules = rules # A->ABC|DEF => {A : [[A,B,C], [D,E,F]]}
        items.append([[0, '', [], [source], 'init']]) # [fromItem, left rule, right rule before point, right rule after point, state]
    def prediction(self, itemNum : int):


def readRules(f) -> dict:
    rules = {}
    l = f.readline()
    while l.split():
        [left, right] = l.replace(' ', '').replace('\n', '').replace('"', '').split(':')
        right = right.split('|')
        rules[left] = [list(r) for r in right]
        l = f.readline()
    return rules


def f1(fileName):
    f = open(fileName, 'r')
    rules = readRules(f)
    l = f.readline().split()
    while l:
        earley = EarleyAlgorithm(l, rules, '0')
        l = f.readline().split()


# ####### MAIN #######
f = 'bis_input.txt'

# Part 1 - Early Algorithm
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

