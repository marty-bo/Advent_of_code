
import time
import os
import re

input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

def apply_move(move_instr:str, stacks:list[list[str]]) -> None:
    instr = [int(e) for e in re.findall(r'\d+', move_instr)]
    for i in range(instr[0]):
        stacks[instr[2]-1].append(stacks[instr[1]-1].pop())
    return stacks

def read_stacks(lines: list[str]) -> list[list[str]]:
    stacks = [[] for i in range((len(lines[0]) + 1) >> 2)]
    for line in lines:
        matches = re.findall(r'    |\[\D\] ', line)
        for id, match in enumerate(matches):
            if match != '    ':
                stacks[id].insert(0, match[1:-2])
    return stacks

def f1():
    f = open(input_file_path)
    lines = f.readlines()
    f.close()

    lines = list(map(lambda l: l.replace('\n', ' ') ,lines))

    id = lines.index(' ')
    stacks_desc = lines[:id]
    moves_desc = lines[id+1:]
    if moves_desc[-1] == ' ':
        moves_desc.pop()

    stacks = read_stacks(stacks_desc)

    for move_instr in moves_desc:
        stacks = apply_move(move_instr, stacks)

    print("Stacks heads are %s" % ''.join([s[-1] for s in stacks]))
    return

print("Begin task 1...")
start_time = time.time()
f1()
print("End task 1 in  %.8s seconds." % (time.time() - start_time))
