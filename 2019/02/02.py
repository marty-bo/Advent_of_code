
import time

def f1(fileName):
    instr = [int(n) for n in open(f).readline().replace('\n', '').split(',')]
    instr[1] = 12
    instr[2] = 2
    pc = 0
    while instr[pc] != 99:
        try:
            rn = instr[pc+1]
            rm = instr[pc+2]
            rd = instr[pc+3]
        except:
            print('Error.')
            break
        if instr[pc] == 1:
            instr[rd] = instr[rn] + instr[rm]
        elif instr[pc] == 2:
            instr[rd] = instr[rn] * instr[rm]
        pc += 4
    return instr[0]


def f2(fileName, target):
    instr_temp = [int(n) for n in open(f).readline().replace('\n', '').split(',')]
    for noun in range(100):
        for verb in range(100):
            instr = instr_temp.copy()
            instr[1] = noun
            instr[2] = verb
            pc = 0
            while instr[pc] != 99:
                try:
                    rn = instr[pc+1]
                    rm = instr[pc+2]
                    rd = instr[pc+3]
                except:
                    print('Error.')
                    break
                if instr[pc] == 1:
                    instr[rd] = instr[rn] + instr[rm]
                elif instr[pc] == 2:
                    instr[rd] = instr[rn] * instr[rm]
                pc += 4
            print(noun, verb, instr[0])
            if instr[0] == target:
                return 100 * noun + verb




# Part 1
f = 'input.txt'
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
f = 'input.txt'
target = 19690720
start_time = time.time()
print(f2(f, target))
print("--- %s seconds ---" % (time.time() - start_time))
