
import time

def f1(fileName):
    file = open(fileName)
    instr = file.readline().replace('\n','').split(',')
    inputV = file.readline().replace('\n','').split()[0]
    pc = 0
    p = list
    ins = list
    while instr[pc] != '99':
        p = list(instr[pc])
        ins = ['0', '0', '0', '0', '0']
        for i in range(len(p)):
            ins[5-len(p)+i] = p[i]
        
        if ins[4] == '1':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            rm = instr[pc+2] if ins[1]=='1' else instr[int(instr[pc+2])]
            rd = int(instr[pc+3])
            instr[rd] = str(int(rn) + int(rm))
            pc += 4
        elif ins[4] == '2':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            rm = instr[pc+2] if ins[1]=='1' else instr[int(instr[pc+2])]
            rd = int(instr[pc+3])
            instr[rd] = str(int(rn) * int(rm))
            pc += 4
        elif ins[4] == '3':
            rn = int(instr[pc+1])
            instr[rn] = inputV
            pc += 2
        elif ins[4] == '4':
            rn = int(instr[pc+1])
            print(instr[rn])
            pc += 2
    return

def f2(fileName):
    file = open(fileName)
    instr = file.readline().replace('\n','').split(',')
    inputV = file.readline().replace('\n','').split()[0]
    pc = 0
    p = list
    ins = list
    while instr[pc] != '99':
        p = list(instr[pc])
        ins = ['0', '0', '0', '0', '0']
        for i in range(len(p)):
            ins[5-len(p)+i] = p[i]
        
        if ins[4] == '1':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            rm = instr[pc+2] if ins[1]=='1' else instr[int(instr[pc+2])]
            rd = int(instr[pc+3])
            instr[rd] = str(int(rn) + int(rm))
            pc += 4
        elif ins[4] == '2':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            rm = instr[pc+2] if ins[1]=='1' else instr[int(instr[pc+2])]
            rd = int(instr[pc+3])
            instr[rd] = str(int(rn) * int(rm))
            pc += 4
        elif ins[4] == '3':
            rd = int(instr[pc+3])
            instr[int(rd)] = inputV
            pc += 2
        elif ins[4] == '4':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            print(rn)
            pc += 2
        elif ins[4] == '5':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            rm = instr[pc+2] if ins[1]=='1' else instr[int(instr[pc+2])]
            if int(rn) != 0:
                pc = int(rm)
            else:
                pc += 3
        elif ins[4] == '6':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            rm = instr[pc+2] if ins[1]=='1' else instr[int(instr[pc+2])]
            if int(rn) == 0:
                pc = int(rm)
            else:
                pc += 3
        elif ins[4] == '7':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            rm = instr[pc+2] if ins[1]=='1' else instr[int(instr[pc+2])]
            rd = int(instr[pc+3])
            if int(rn) < int(rm):
                instr[rd] = '1'
            else:
                instr[rd] = '0'
            pc += 4
        elif ins[4] == '8':
            rn = instr[pc+1] if ins[2]=='1' else instr[int(instr[pc+1])]
            rm = instr[pc+2] if ins[1]=='1' else instr[int(instr[pc+2])]
            rd = int(instr[pc+3])
            if int(rn) == int(rm):
                instr[rd] = '1'
            else:
                instr[rd] = '0'
            pc += 4
    return




# Part 1
f = 'input_1.txt'
start_time = time.time()
f1(f)
print("--- %s seconds ---" % (time.time() - start_time))



# Part 2
f = 'input_2.txt'
start_time = time.time()
f2(f)
print("--- %s seconds ---" % (time.time() - start_time))
