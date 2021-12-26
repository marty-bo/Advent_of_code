
from os import close
import time

CHUNKS = {'(':')','[':']','{':'}','<':'>'}
CORRUPTED_SCORE = {')':3,']':57,'}':1197,'>':25137}
COMPLETION_SCORE = {')':1,']':2,'}':3,'>':4}
OPEN_CHAR = '([{<'
CLOSE_CHAR = ')]}>'



def is_corrupted(line):
    stack = []
    for char in line:
        if char in OPEN_CHAR:
            stack.append(char)
        elif char in CLOSE_CHAR:
            if CHUNKS.get(stack[-1], '') == char:
                stack.pop()
            else:
                return CORRUPTED_SCORE.get(char, 0)
    return 0

def complete(line):
    stack = []
    for char in line:
        if char in OPEN_CHAR:
            stack.append(char)
        elif char in CLOSE_CHAR:
            if CHUNKS.get(stack[-1], '') == char:
                stack.pop()
            else:
                return ''
    res = []
    for char in stack[::-1]:
        res.append(CHUNKS.get(char, '-'))
    return res

def completion_score(completion):
    score = 0
    for c in completion:
        score *= 5
        score += COMPLETION_SCORE.get(c, 0)
    return score

def f1():
    count = 0
    f = open('input.txt')
    for line in f.readlines():
        line = line.replace('\n', '')
        count += is_corrupted(line)
    print('[f1]: Count = %d' % (count))
    return
    

def f2():
    f = open('input.txt')
    scores = []
    for line in f.readlines():
        line = line.replace('\n', '')
        if is_corrupted(line) == 0:
            completion = complete(line)
            scores.append(completion_score(completion))
    scores.sort()

    print('[f2]: Middle score = %d' % (scores[int(len(scores)/2)]))
    return
    


print("########################################")
start_time = time.time()
f1()
print("--------- %.7s seconds ---------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f2()
print("--------- %.7s seconds ---------" % (time.time() - start_time))

