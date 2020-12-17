
import time



def f1(fileName):
    f = open(fileName, 'r')
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    mem = {}
    for l in f.readlines():
        if l[:2] == 'ma':
            mask = l[7:]
        else:
            memAdr = l[4:].split(']')[0]
            val = int(l.split()[-1])
            res = 0
            for i in range(36):
                res |= (1 if mask[35-i] == '1' else 0 if mask[35-i] == '0' else (val >> i) & 1) << i
            mem[memAdr] = res
    return sum(mem.values())







def generateMemAdr(mask, memAdr):
    nb = 1
    for c in mask:
        if c == 'X':
            nb *= 2
    if nb == 1:
        return mask
    res = []
    for i in range(nb):
        bitPos = 0
        tmp = memAdr
        for j in range(len(mask)-1, -1, -1):
            if mask[j] == 'X':
                if (i >> bitPos) & 1:
                    tmp |= 1 << (35-j)
                else:
                    tmp &= ~(1 << (35-j))
                bitPos += 1
            elif mask[j] == '1':
                tmp |= 1 << (35-j)
        res.append(tmp)
    return res



def f2(fileName):
    f = open(fileName, 'r')
    mask = ''
    masks = []
    mem = {}
    for l in f.readlines():
        if l[1] == 'a':
            mask = list(l.split()[2])
        else:
            memAdr = int(l[4:].split(']')[0])
            adr = generateMemAdr(mask, memAdr)
            val = int(l.split()[2])
            for a in adr:
                mem[a] = val
    return sum(mem.values())




# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2(f))
print("--- %s seconds ---" % (time.time() - start_time))

