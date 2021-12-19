
import time
from Paper import Paper

def f():

    f = open('input.txt')

    # read dots
    dots = set()
    line = f.readline()
    while line != '\n':
        line = line.replace('\n', '').split(',')
        dots.add((int(line[0]), int(line[1])))
        line = f.readline()
    
    # read fold instructions
    fold_instructions = list()
    line = f.readline()
    while line != '':
        line = line.replace('\n', '').split('=')
        fold_instructions.append((line[0][-1], int(line[1])))
        line = f.readline()
    print(fold_instructions)

    f.close()

    # PART I
    # fold with the first instruction
    paper = Paper(dots)
    paper.fold(fold_instructions.pop(0))
    # print the number of visible dot
    print('[f]: Dot count = %d' % (paper.count_dots()))

    # PART II
    # fold with the other instructions
    for fold_instruction in fold_instructions:
        paper.fold(fold_instruction)
    # print the result paper
    print(paper.to_string())

    return 0
    



print("########################################")
start_time = time.time()
f()
print("----------- %.8s seconds -----------" % (time.time() - start_time))
